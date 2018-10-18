import boto3
from decouple import config
from pprint import pprint


# Definição do perído a ser consultado
time_period = {
'Start': '2018-06-01',
'End': '2018-07-01' # Data final é exclusiva, sempre devemos usar
                    # o primeiro dia depois do período desejado
}

# Opções de agrupamento
group_by = [
{
'Type': 'TAG',
'Key': 'Name'
},
{
'Type': 'DIMENSION',
'Key': 'USAGE_TYPE'
}
]

# Instanciando o cost explorer com o boto3
cost_explorer = boto3.client('ce',
                            aws_access_key_id = config('AWS_IAM_ACCESS_KEY'),
                                aws_secret_access_key = config('AWS_IAM_SECRET_KEY'))


# Efetuando a consulta
results = cost_explorer.get_cost_and_usage(TimePeriod=time_period,
Granularity='MONTHLY',
Metrics=['BlendedCost','UnblendedCost', 'UsageQuantity'],
GroupBy = group_by
)
pprint(results)
