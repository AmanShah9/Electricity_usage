

def get_exchange_data() -> List[Dict[str, Any]]:
    url = 'https://meter-api.isocietymanager.com/v1/society/99/exportreading?api-token=3a980a33acd7b7d17954f8b422dd04d435f0d7d66af450b281ecd9e8c45f3934&user-id=112553&from_date=2022-06-11&to_date=2022-06-18&unit=AZJ0205&type=xls'
    try:
        r = requests.get(url)
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
        sys.exit(1)
    return r.json().get('data', [])