class Helper():
    def __init__(self):
        self.list = 'poll, anime, [time, settimezone], blackjack, [money, loan, debt, pay], log'
    def execute(self, dict):
        if len(dict['message']) <= 6:
            dict['message'] = 'Type $help <command> for details.\r\n%s %s :%s.' %(dict['type'],dict['channel'],self.list)
            return dict
        elif len(dict['message']) > 6:
            option = dict['message'][6:]
            if option.startswith('poll'):
                dict['message'] = '$poll <question> starts a poll with <question>.'
            elif option.startswith('anime'):
                dict['message'] = '$anime <title> gives the time left until the next subbed episode of <title> is released. Some short forms of <title> are accepted.'
            elif option.startswith('time'):
                dict['message'] = '$time <person> displays the current time in <person>\'s time zone. Leaving <person> blank gives user\'s own time. Only works when time zone is set.'
            elif option.startswith('settimezone'):
                dict['message'] = '$settimezone <number> sets your time zone to UTC +/- <number>.'
            elif option.startswith('blackjack'):
                dict['message'] = '$blackjack starts a game of blackjack. Minimum of 1 NanoDollar required.'
            elif option.startswith('money'):
                dict['message'] = '$money displays the amount of NanoDollars you have under your nick. (Everyone starts with 10.)'
            elif option.startswith('loan'):
                dict['message'] = 'When you are in need of money, use $loan <number> to request for one. Note that you cannot use $loan when in $debt, and having one can limit your rights.'
            elif option.startswith('debt'):
                dict['message'] = '$debt displays the amount of money you currently owe. Having a $debt severely limits your rights.'
            elif option.startswith('pay'):
                dict['message'] = '$pay <number> pays off <number> from your debt. Note that you do not need to repay your debt in full.'
            elif option.startswith('log'):
                dict['message'] = '$log generates a log of messages you\'ve missed since you last left the channel. Requires a time zone to be set.'
            else:
                dict['message'] = 'Type $help <command> for details.\r\n%s %s:' %(dict['type'],dict['channel']) + self.list
            return dict