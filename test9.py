def insert_sql(table, **kwargs):
    return 'insert into {} ({}) values ({})'.format(table, my_join(",", *kwargs.keys()), my_join(',', *kwargs.values()))
    # return 'insert into %s (%s) values (%s)' %(table, my_join(",", *kwargs.keys()), my_join(',', *kwargs.values()))


def my_join(string, *args):
    return string.join(['"' + arg + '"' if isinstance(arg, str) else str(arg) for arg in args])


if __name__ == '__main__':
    dd = dict(
        name='李寻欢',
        age=35,
        stunt="小李飞刀，例不虚发",
    )
    import time
    print(insert_sql('User', id=1, usercode="admin", password="uJ45aIeS9N80kaSFDjvk%2FA%3D%3D", username="系统管理员",
                     role='1', sectorid=99, projectid=0))
    print(insert_sql('name', id=1, name="lixunhuan", age=18, create_time=time.time()))

    print(insert_sql('xiaoli', **dd))
