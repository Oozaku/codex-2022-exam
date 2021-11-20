# Description

Hear we are going to design a model for a simple Order Management System involving mainly the
following entities: Clients; Products; Orders.


# Solution

## Client

For the client, we need his identity information that will be mainly CPF and his full name.
Other field is *UserId*, created when the account is created in database and it is the primary key
that will be used throughout the platform. The *AddressId* is the foreign key to the client's 
address.

| <u>UserId</u> | CPF            | Full Name | Fone Number        | Email           |
|---------------|----------------|-----------|--------------------|-----------------|
| 123           | 000.000.000-00 | João      | +55 (12) 1234-5678 | joao@gmail.com  |
| 456           | 123.456.789-10 | Maria     | +55 (89) 0213-2356 | maria@gmail.com |


### Address

One other information that we need from client is his address, but as it has a lot of fields
that would pollute the *Client* entity, Adddress will be an entity by itself and *UserId* is the
foreign key to *Client* The last important detail is that one client can have more than one address 
and one address may have more than one client.

| UserId | Street Number | Number | CEP       |
|--------|---------------|--------|-----------|
| 123    | rua Lalala    | 123    | 12345-678 |
| 456    | rua Lalala    | 123    | 12345-678 |

There are other informations about the client, as the login information, but I think it's not relevant
to solve this exercise. The only idea that we need to know is that after a successful login, they will
find the corresponding client with the key *UserId*.

## Order

Each order has an unique *OrderId* created when a order is created and it is the primary key.
Other field that is important to mention is that *Order* has the field *UserId* that points to
only one client, that is one order has only one client, but one client may have more than one 
order.

| <u>OrderId</u> | UserId | Date       |
|----------------|--------|------------|
| 123            | 123    | 01/01/2021 |
| 456            | 123    | 05/06/2021 |
| 789            | 456    | 24/08/2021 |
|                |        |            |

### Cart

As one order may have more than one product, the solution is to make a new table and to see 
what products were bought in an order, we filter for all entries that have OrderId equal to
what we are looking for, like the order 789 has three products in the cart.

Other field that is important is price, since we need to know the price tag in the exact
moment that the client have finished the buy and not the most current price tag for that 
product.

| OrderId | Barcode  | Price |
|---------|----------|-------|
| 123     | 00000000 | 25.65 |
| 456     | 00543103 | 43.89 |
| 789     | 00000000 | 25.65 |
| 789     | 00543103 | 43.89 |
| 789     | 32486801 | 43.41 |

## Product

Each product has an unique bar code and it is the primary key. Also it holds the product's
name and the current price of the product.

| <u>Barcode</u> | Name      | Price |
|----------------|-----------|-------|
| 00000000       | Pendrive  | 30.34 |
| 00543103       | SSD 240GB | 40.43 |
| 32486801       | RAM 8GB   | 54.64 |

# Extras

## SQL

"List ORDERS with number of items"
~~~sql
SELECT O.OrderId, O.UserId, O.Date, Count(*) AS NUMBER_OF_ITEMS
    FROM ORDER O, CART C
    WHERE O.OrderId = C.OrderId
    GROUP BY O.OrderId, O.UserId, O.Date
~~~

## Indexes

"Which indexes should be created in this model?"

In this model, the indexes that should be created to guarantee faster searches in our databases
are *UserId*, *OrderId* and *Barcode*. Because every model in this database uses one of these 
fields and with them we can make the most powerful and common queries faster. For example, one
query that I think that it is important is "who bought the item with barcode 00000000?", because
there may be a recall from the manufacture and we need to take action fast to recover the defective
products. 

