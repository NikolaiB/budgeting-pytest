## Test Plan

This Test Plan describes the functional and automated test cases that are conducted on the Budget app.

**Function Testing**
-
We have to verify that all functionality works as expected. 
For the Budget and Reports pages: The system has to be able to:

- Add a new category with category(Income,Taxes), description and amount fields. Working balance should be changed, 
Inflow vs Outflow chart and Spending by Category should be also changed.
- Update an existing item, button update should be enable and working balance should be changed accordingly. 
Should be tested for positive and negative Working Balance. Inflow vs Outflow chart and Spending by Category should be 
also changed.
- Remove an existing item, button remove should be enable and working balance should be changed accordingly. 
Inflow vs Outflow chart and Spending by Category should be also changed.
- Cancel the updating process. Button cancel should be enable.
- Add a new item without description. Button Add should be disabled.
- Add a new item without amount field. Button Add should be disable.

**Automated Testing**
-
The Smoke scope has to include the most important base functionality and be applied for:

- Add a new item.
- Update an item.
- Delete the item.