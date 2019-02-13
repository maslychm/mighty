# Print information about the server

from datetime import datetime, date
import holidays
import calendar

def serverinfo(client, message):

    guild = message.guild
    guildname = guild.name
    membernum = guild.member_count
    now = datetime.today()
    month = calendar.month_name[now.month]

    ret = f"As of {month} {now.day} of {now.year} **{guildname}** has {membernum} members"

    us_holidays = holidays.UnitedStates()
    nowstr = now.strftime("%m-%d-%Y")

    if nowstr in us_holidays:
        ret += "\nAlso, today is {}".format(us_holidays.get(nowstr))

    return ret
