# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

import collections
# key : table , val: dict of items
class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """

        tables_orders = collections.defaultdict(dict)
        # default dict allows for creation of new keys without key/val err
        items = set()
        # set is kinda like a list, mutable, but cannot have duplicates
        result = []

        for customer, table, item in orders:
            if item in tables_orders[table].keys():
                tables_orders[table][item] += 1
            else:
                tables_orders[table][item] = 1
            items.add(item)

        result.append(sorted(items))

        # lambda is used for creating anonymous functions
        # in this case, take each key x from tables_orders.keys and convert to integer
        # so, get the keys, turn the keys into integers, and then finally sort the keys
        for key in sorted(tables_orders.keys(), key = lambda x: int(x)):
            a_table_order = tables_orders[key] # a singular tables order
            row = [str(key)]    # the table no. in string form

            for item in result[0]:
                if item in a_table_order:
                    row.append(str(a_table_order[item]))
                    # add amount of item # to row
                else:
                    row.append("0")
                    # add 0 for item not ordered
            result.append(row)
        result[0] = ["Table"] + result[0]
        return result



