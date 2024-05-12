import requests

# Function to fetch account posting authorization for a target
def get_account_auths(target):
    # Define API endpoint for fetching account auths
    api_endpoint = "https://sds.steemworld.org/authorities_api/getAccountAuthsByTarget"

    try:
        # Construct the full URL
        url = f"{api_endpoint}/{target}"

        # Send GET request
        response = requests.get(url)
        if response.status_code == 200:
            # Extract and return account authorization details
            return response.json()
        else:
            print(f"Failed to fetch account auths for {target}: {response.reason}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching account auths for {target}:", e)
        return None

# Function to fetch account details for a given username
def get_account_details(username):
    # Define API endpoint for fetching account details
    api_endpoint = "https://sds.steemworld.org/accounts_api/getAccount"

    try:
        # Construct the full URL
        url = f"{api_endpoint}/{username}"

        # Send GET request
        response = requests.get(url)
        if response.status_code == 200:
            # Extract and return account details
            return response.json()
        else:
            print(f"Failed to fetch account details for {username}: {response.reason}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching account details for {username}:", e)
        return None

# Main function
def main():
    # Define the target for which to fetch account auths
    target = "woxauto"

    # Fetch account posting authorization for the target
    account_auths = get_account_auths(target)
    if account_auths and 'result' in account_auths and 'rows' in account_auths['result']:
        # Extract account names from the authorization response
        accounts = [auth[1] for auth in account_auths['result']['rows']]

        # Fetch and print total vests for each account above 1,500,000
        for account in accounts:
            try:
                account_details = get_account_details(account)
                if account_details and 'result' in account_details:
                    vesting_shares = float(account_details['result']['vesting_shares'])
                    received_vesting_shares = float(account_details['result']['received_vesting_shares'])
                    delegated_vesting_shares = float(account_details['result']['delegated_vesting_shares'])
                    total_vests = vesting_shares + received_vesting_shares - delegated_vesting_shares
                    if total_vests > 15000000:
                        print(f"Account: {account}, Total Vests: {total_vests}")
                else:
                    print(f"Failed to fetch account details for {account}")
            except KeyboardInterrupt:
                print("\nProgram interrupted by user. Exiting...")
                break
    else:
        print(f"Failed to fetch account auths for {target}")

if __name__ == "__main__":
    main()
