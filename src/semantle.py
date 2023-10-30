import pandas as pd


class Tracker:
    def __init__(self):
        self.dict = {}
        self.df = None
        self.query_func = self._raise

    def query(self, input_data):
        if input_data in self.dict:
            return self.dict[input_data]

        out = self.query_func(input_data)

        if "flag" in out:
            raise RuntimeError(f"Found the flag using '{input_data}' as input!")

        self.dict[input_data] = out["message"]

        return out

    def top(self, n=10):
        self.df = pd.DataFrame(
            {
                "word": self.dict.keys(),
                "score": self.dict.values(),
            }
        )
        return self.df.sort_values(by="score", ascending=False).head(n)

    @staticmethod
    def _raise(*args, **kwargs):
        raise ValueError("No query function set")


if __name__ == "__main__":
    tracker = Tracker()

    import requests

    input_data = "attention"

    def query(input_data):
        response = requests.post(
            "http://semantle.advml.com/score",
            json={"data": input_data},
        )
        return response.json()

    tracker.query_func = query

    tracker.query("attention")
    tracker.query("transformer")
    tracker.query("article")
    tracker.query("an")
    tracker.query("a")
    tracker.query("actual")
    tracker.query("astro")  # That was a big bump
    tracker.query("atrology")
    tracker.query("astronomy")
    tracker.query("astronomical")
    tracker.query("astronom")
    tracker.query("scientist")
    tracker.query("astrophysics")
    tracker.query("stars")
    tracker.query("sun")
    tracker.query("study")
    # And other words related to astro...
    tracker.query("asteroid")  # That's it :)
