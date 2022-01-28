def time_difference(self):
    a = self.created
    b = self.updated
    created = a.year + a.month + a.day + a.hour + a.minute + a.second
    updated = b.year + b.month + b.day + b.hour + b.minute + b.second
    difference = int(updated) - int(created)
    return abs(difference)