#problem 1.7 (!!!Klar)
months = int(input("Amount of months the servers will be used: "))
server_purchase = [1790, 2300, 3200, 5000, 8900]
to_run_a_server = 100
cost_running_servers = 100*5*months
cost = 0
for harware in server_purchase:
    average_cost = harware // months + to_run_a_server
    print(f"The server costing {harware} costs on average {average_cost} each month.")
#Total Cost 
    cost = sum(server_purchase)
    total_cost = cost + cost_running_servers
print(f"The totalt cost running the server for {months} months is {total_cost}.")