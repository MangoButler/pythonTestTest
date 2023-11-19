def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        return 'wrong'
    except ValueError as err:
        return err
    except TypeError as err:
        return err
    except Exception as err:
        return f'Something went wrong: {err} {type(err)}'


if __name__ == '__main__':
    print(do_stuff(4))
    print('not stopping')

