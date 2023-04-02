import pandas


def main(user_csv, device_csv, device_names):
    df = pandas.read_csv(user_csv)
    df_2 = pandas.read_csv(device_csv)

    emails = df['email']
    first_names = df['first_name']
    last_names = df['last_name']

    for email, first_name, last_name in zip(emails, first_names, last_names):
        print(f'Converting {first_name} {last_name}')
        df_2.loc[df_2[device_names] == f'{first_name} {last_name}', device_names] = email

    df_2.to_csv(device_csv)


if __name__ == '__main__':
    main('lumos_labs_users - lumos_labs_users.csv', 'LumosLabsDeviceInventory - LumosLabsDeviceInventory.csv', 'Assignee')