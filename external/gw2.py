import requests


class GW2(object):
    """
    Wrapper for guildwars2 api
    """

    def __init__(self, auth):
        b = "Bearer " + auth
        self.headers = {"Authorization": b}

    def get_raid_kills(self):
        """
        Returns the current raid kills of the week
        """
        url = "https://api.guildwars2.com/v2/account/raids"
        r = requests.get(url, headers=self.headers)
        return r.json()

    def get_t4_daily(self):
        """
        Returns a JSON of t4 daily
        """
        url_daily = "https://api.guildwars2.com/v2/achievements/daily"
        url_category = "https://api.guildwars2.com/v2/achievements"
        daily = requests.get(url_daily, headers=self.headers)
        daily = daily.json()
        fractals = daily['fractals']
        urls = ["{}?id={}".format(url_category, f['id']) for f in fractals]

        # Get individual result
        fd = []
        for url in urls:
            r = requests.get(url, headers=self.headers)
            r = r.json()
            fd.append(r)

        fd_dict = {}
        count = 0
        for f in fd:
            frac_text = "at fractal scale 76"
            find_inside = frac_text in f['requirement']

            if find_inside:
                fd_dict[count] = f["name"]
                count += 1
        return fd_dict
