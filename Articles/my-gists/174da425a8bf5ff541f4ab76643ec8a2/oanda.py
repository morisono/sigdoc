

from oandapyV20.endpoints import orders, positions
from oandapyV20 import API
import datetime


class fx_trader:
    def __init__(self, account_id, access_token, instrument="USD_JPY", environme
nt="practice"):
        # 変数定義
        self.instrument = instrument
        self.account_id = account_id
        self.access_token = access_token
        self.log = []

        # API用のクラスを定義
        self.client = API(access_token=access_token, environment=environment)

    def logging(self, text):
        logText = "[{}] {}".format(datetime.datetime.now().strftime("%Y/%m/%d %
H:%M:%S"), text)
        print(logText)
        self.log.append(logText)

        return

    def order(self, unit):
        # 売買注文の内容を設定
        self.data = {
          "order": {
            "units": unit,
            "instrument": self.instrument,
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        }

        # 売買注文
        self.r = orders.OrderCreate(accountID=account_id, data=self.data)
        self.res = self.client.request(self.r)

        self.logging("new entry: {} at {}".format(unit, self.res.get("orderFillT
ransaction").get("price")))
        return

    def positions(self):
        # 保有ポジションを取得
        self.r = positions.PositionDetails(accountID=self.account_id, instrument
=self.instrument)
        self.res = self.client.request(self.r)

        # ロングとショートの保有数を抽出
        self.longPositionUnits = int(self.res.get("position").get("long").get("u
nits"))
        self.shortPositionUnits = int(self.res.get("position").get("short").get
("units"))

        #　結果を表示
        print("longPositionUnits", self.longPositionUnits)
        print("shortPositionUnits", self.shortPositionUnits)

        return

    def close(self):
        # ポジションをクローズ
        if self.longPositionUnits != 0:
            data = {"longUnits": "ALL"}
            self.r = positions.PositionClose(accountID=self.account_id, instrume
nt=self.instrument, data=data)
            self.res = self.client.request(self.r)

            self.logging("position close: {} at {}. pl: {}".format(
                fx.res.get("longOrderFillTransaction").get("units"),
                fx.res.get("longOrderFillTransaction").get("price"),
                fx.res.get("longOrderFillTransaction").get("pl"),
            ))

        if self.shortPositionUnits != 0:
            data = {"shortUnits": "ALL"}
            self.r = positions.PositionClose(accountID=self.account_id, instrume
nt=self.instrument, data=data)
            self.res = self.client.request(self.r)

            self.logging("position close: {} at {}. pl: {}".format(
                fx.res.get("shortOrderFillTransaction").get("units"),
                fx.res.get("shortOrderFillTransaction").get("price"),
                fx.res.get("shortOrderFillTransaction").get("pl"),
            ))

        return

