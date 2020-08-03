industry_list = [
    {
        "parent_ind": "女装",
        "name": "连衣裙"
    },
    {
        "name": "女装"
    },
    {
        "parent_ind": "女装",
        "name": "半身裙"
    },
    {
        "parent_ind": "女装",
        "name": "A字裙"
    },
    {
        "name": "数码"
    },
    {
        "parent_ind": "数码",
        "name": "电脑配件"
    },
    {
        "parent_ind": "电脑配件",
        "name": "内存"
    },

]


def convert_format(data):
    industry_tree = {}
    for ind in industry_list:
        parent_ind = ind.get("parent_ind")
        name = ind.get("name")
        if parent_ind:
            if (func(industry_tree, parent_ind, name)):
                industry_tree[parent_ind] = {name:{}}

        elif not industry_tree.get(name):
            industry_tree[name] = {}
    return industry_tree


def func(dic, parent_ind, name):
    if not dic: return True
    for key in dic.keys():
        if key == parent_ind:
            dic[key].update({name: {}})
            return False
        func(dic[key], parent_ind, name)
    return True


if __name__ == '__main__':
    print(convert_format(industry_list))
