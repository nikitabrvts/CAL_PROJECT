from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Boolean, ForeignKey, PrimaryKeyConstraint, DDL, event


# Данные для подключения к БД.
# Данные нужно указать свои. 
dbname = 'postgres'
user = 'postgres'
password = '123'
host = 'localhost'

# Создание соединения с базой данных
engine = create_engine(f'postgresql://{user}:{password}@{host}/{dbname}')

# Создание объекта MetaData
metadata = MetaData()

# Создание таблицы client
client_table = Table('client', metadata,
    Column('client_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50)),
    Column('surname', String(50)),
    Column('middle_name', String(50)),
    Column('phone_number', String(11)),
    Column('email', String(50))
)

# Создание таблицы authorisation
authorisation_table = Table('authorisation', metadata,
    Column('manager_id', Integer, primary_key=True, autoincrement=True),
    Column('login', String(25)),
    Column('password_hash', Text),
    Column('boss', Boolean)
    )

# Создание таблицы contract
contract_table = Table('contract', metadata,
    Column('contract_id', Integer, autoincrement=True, primary_key=True),
    Column('client_id', Integer, ForeignKey('client.client_id')), 
    Column('manager_id', Integer, ForeignKey('authorisation.manager_id'))
)

# Создание таблицы invested
invested_table = Table('invested', metadata,
    Column('contract_id', Integer, ForeignKey('contract.contract_id')),
    Column('rent', Integer),
    Column('repair', Integer),
    Column('equipment', Integer),
    Column('products', Integer),
    Column('documents', Integer),
    Column('salary', Integer),
    Column('security', Integer),
    Column('publicity', Integer),
    Column('utility_costs', Integer),
    Column('taxes', Integer)
    )

# Создание таблицы expenses
expenses_table = Table('expenses', metadata,
    Column('contract_id', Integer, ForeignKey('contract.contract_id')),
    Column('month', Integer),
    Column('rent', Integer),
    Column('repair', Integer),
    Column('products', Integer),
    Column('salary', Integer),
    Column('security', Integer),
    Column('publicity', Integer),
    Column('utility_costs', Integer),
    PrimaryKeyConstraint('contract_id', 'month')
    )

# Создание таблицы income
income_table = Table('income', metadata,
    Column('contract_id', Integer, ForeignKey('contract.contract_id')),
    Column('month', Integer),
    Column('visitor_count', Integer),
    Column('avg_check', Integer),
    PrimaryKeyConstraint('contract_id', 'month')
    )

# Создание таблицы payback
payback_table = Table('payback', metadata,
    Column('contract_id', Integer, ForeignKey('contract.contract_id'), primary_key=True),
    Column('client_id', Integer, ForeignKey('client.client_id')),
    Column('count_month', Integer)
    )

# Создание таблицы result
result_table = Table('result', metadata,
    Column('result_id', Integer, primary_key=True, autoincrement=True),
    Column('client_id', Integer),
    Column('contract_id', Integer)
    )

# Создание таблицы review
review_table = Table('review', metadata,
    Column('review_id', Integer, primary_key=True, autoincrement=True),
    Column('contract_id', Integer, ForeignKey('contract.contract_id')),
    Column('text_review', Text)
)

# Определение DDL для создания триггера
# чтобы поле month зависило от поля contract_id
# и месяца начинались с 1 для каждого различного contract_id
expenses_trigger_ddl = DDL('''
CREATE OR REPLACE FUNCTION expenses_update_month() RETURNS TRIGGER AS $$
BEGIN
    NEW.month := (SELECT COALESCE(MAX(month), 0) + 1 FROM expenses WHERE contract_id = NEW.contract_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_month_trigger
BEFORE INSERT ON expenses
FOR EACH ROW
EXECUTE FUNCTION expenses_update_month();
''')

income_trigger_ddl = DDL('''
CREATE OR REPLACE FUNCTION income_update_month() RETURNS TRIGGER AS $$
BEGIN
    NEW.month := (SELECT COALESCE(MAX(month), 0) + 1 FROM income WHERE contract_id = NEW.contract_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_month_trigger
BEFORE INSERT ON income
FOR EACH ROW
EXECUTE FUNCTION income_update_month();
''')

# Создание триггеров
event.listen(expenses_table, 'after_create', expenses_trigger_ddl)
event.listen(income_table, 'after_create', income_trigger_ddl)

metadata.create_all(engine)