# Author:xqkang
# Date:2020/10/9 下午12:00

def file_db_handle(conn_params):
    '''
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    '''
    # print(">>>>>>file db:", conn_params)
    db_path = '%s/%s/'%(conn_params['path'], conn_params['name'])
    return db_path

def db_handler(conn_parms):
    '''
    connect to db
    :param conn_parms: the db connection params set in settings
    :return:a
    '''

    if conn_parms['engine'] == 'file_stotage':

        return file_db_handle(conn_parms)
    elif conn_parms['engine'] == 'mysql':
        pass #todo list

