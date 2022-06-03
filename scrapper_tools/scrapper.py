import random
import numpy as np
import pandas as pd
import requests
from urllib.parse import urlparse, ParseResult
from requests_html import HTMLSession, HTML
from typing import Any, Optional, Tuple
from dataclasses import dataclass, InitVar
from pathlib import Path
from .logging import logger, LogConfig
from .url import URL


class WebScrapperException(BaseException):
    pass

class WebScrapperCantFind(WebScrapperException):
    pass

@dataclass
class URL(object):
    url: InitVar[str]=None

    def __post_init__(self, url: str) -> str:
        self.url = url
        ( self.is_valid,
            self.scheme,
            self.netloc,
            self.path,
            self.params,
            self.query,
            self.fragment ) = self.__validator(url)

    def validator(self, url: str) -> bool:
        return self.__validator(url)[0]

    def __validator(self, url: str) -> Tuple[bool,
                                           str, str, str, str, str, str]:

        try:
            v = urlparse(url)
            v = ( all([v.scheme, v.netloc]),
                  v.scheme, v.netloc, v.path, v.params, v.query, v.fragment)
        except:
            v = False
            v = (v, '', '', '', '', '', '')
        return v

    def __repr__(self) -> str:
        return str(self.url)

class Scrapper(object):
    def __init__(self,
                 timeout: Optional[int]=0,
                 sleep: Optional[int]=10,
                 max_count: Optional[int]= 5,
                 max_user_agents: int=10,
                 logconfig: Optional[LogConfig]=None,
        ):
        self.timeout = timeout
        self.sleep = sleep
        self.max_count = max_count
        self.columns = list()
        self.values = list()
        self.df = pd.DataFrame()
        self.user_agents = pd.DataFrame()
        self.max_user_agents = max_user_agents
        self.headers = {"User-Agent": self.get_random_user_agent() }
        self.session = None
        self.response = None

        if logconfig:
            logger.remove()
            logger.configure(**logconfig)
            logger.debug(f'LOG configure: {logconfig}')
        else:
            logger.disable(__name__)

    def get_random_user_agent(self) ->str:
        if self.user_agents.empty:
            data_file  = Path(__file__).parent / 'data/user_agents.csv'
            self.user_agents = pd.read_csv(data_file,
                                        header=[0],
                                        nrows=self.max_user_agents)
            self.max_user_agents = len(self.user_agents)
        choose_idx = int(np.random.choice(self.max_user_agents,
                                          replace=True, size=1))
        return self.user_agents.iloc[choose_idx, 1]

    def request(self,
                url: URL,
                timeout: int=None,
                sleep: int=None,
                max_count: int=None,
            ):
            self.timeout = timeout or self.timeout
            self.sleep = sleep or self.sleep
            self.max_count = max_count or self.max_count
            self.url = url

            try:
                self.session = HTMLSession()
                self.session.headers.update(self.headers)
                logger.debug(f'URL: {url}')
                self.response = self.session.get(url)
                logger.debug(f'response status_code: {self.response.status_code}')
                self.response.html.render(timeout=self.timeout,
                                          sleep=self.sleep)
                return self.response
            except requests.exceptions.RequestException as e:
                self.logger.exception("request failed")

    def ommit_char(self, values, omits):
            omit_map = ((x, '') for x in omits)
            for n in range(len(values)):
                values[n] = values[n].replace(*omit_map)
            return values

    def add_df(self, values, columns, omits = None):
            if omits is not None:
                values = self.omit_char(values,omits)
                columns = self.omit_char(columns,omits)

            # Since Pandas 1.3.0
            df = pd.DataFrame(values,index=columns)._maybe_depup_names(columns)
            self.df = pd.concat([self.df,df.T])
