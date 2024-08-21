# payment-processing

- The application consist of multiple payment methods
- Each payment method has its own fees amount/percentage
- Strategy design patterns is used for payment implementation, sense it's different type of the same process
- The application supports multiple discount strategies, which are also implemented using strategy design pattern
- For business logging, I created a class called **Logger**, which designed and implemented using singleton design pattern, ensuring only one instance is creeated from **Logger** class
- **Logger** class implementation is as simple as possible, it justs print message to the console, for real life cases, it is supposed to send logs to logging database
- The application code complies with SOLID principles 
- For currency conversion, the system's default currency is ILS, if the customer want to pay using another currency, the currency type should be passed as parameter to *payment_processing* method