| Q# | Question                                                                                         | Category |
| -- | ------------------------------------------------------------------------------------------------ | -------- |
| 1  | What are the common toppings of a Margherita Pizza?                                              | IND      |
| 2  | Is a FourCheesePizza considered a VegetarianPizza?                                               | SUB      |
| 3  | What toppings make a pizza classified as a HotAndSpicyPizza?                                     | SUB      |
| 4  | Which pizzas contain both MushroomTopping and MozzarellaTopping?                                 | PROP     |
| 5  | Can a pizza have both HamTopping and AnchovyTopping without violating any disjoint restrictions? | DISJ     |
| 6  | What makes a pizza incompatible with a ThinAndCrispyBase?                                        | DISJ     |
| 7  | What topping is classified as both spicy and vegetarian?                                         | LOGIC    |
| 8  | Which pizzas are defined to contain exactly two toppings?                                        | CARD     |
| 9  | Are there any pizzas that are both AmericanPizza and VegetarianPizza?                            | SUB      |
| 10 | Which toppings are disjoint with CheeseTopping?                                                  | DISJ     |
| 11 | Is a QuattroFormaggiPizza classified as a CheesePizza?                                           | SUB      |
| 12 | What toppings are used in a SloppyGiuseppePizza?                                                 | IND      |
| 13 | What distinguishes a VegetarianPizza from a NonVegetarianPizza?                                  | SUB      |
| 14 | Which pizzas are defined to have a DeepPanBase?                                                  | PROP     |
| 15 | What type of base is used in a SoHoPizza?                                                        | IND      |
| 16 | Can a pizza have both PrawnTopping and ChickenTopping?                                           | DISJ     |
| 17 | What is the minimum number of toppings on a SupremePizza?                                        | CARD     |
| 18 | Is a VenezianaPizza suitable for vegetarians?                                                    | SUB      |
| 19 | What spicy meat topping is commonly found on American-style pizzas?                              | IND      |
| 20 | Which pizzas include OliveTopping as one of their ingredients?                                   | PROP     |
| 21 | Are there any pizzas defined to be both HotAndSpicy and Vegetarian?                              | SUB      |
| 22 | What kind of topping is RocketTopping categorized as?                                            | SUB      |
| 23 | Can a pizza be both a SeafoodPizza and a VegetarianPizza?                                        | DISJ     |
| 24 | What are the common toppings on a NapolitanaPizza?                                               | IND      |
| 25 | What is the difference between a TomatoTopping and a SundriedTomatoTopping?                      | SUB      |
| 26 | What toppings are considered disjoint from MeatTopping?                                          | DISJ     |
| 27 | What class of pizza does an AmericanHotPizza belong to?                                          | SUB      |
| 28 | Can a pizza have more than one type of cheese topping?                                           | CARD     |
| 29 | Which pizzas are built using a ThinAndCrispyBase?                                                | PROP     |
| 30 | Is there a pizza that includes both CaperTopping and AnchovyTopping?                             | PROP     |
| 31 | Which pizzas use GarlicTopping as an ingredient?                                                 | PROP     |
| 32 | What toppings are only allowed on a VegetarianPizza?                                             | DISJ     |
| 33 | Is ArtichokeTopping considered a vegetable topping?                                              | SUB      |
| 34 | Which pizzas contain more than three toppings?                                                   | CARD     |
| 35 | What distinguishes a MeatTopping from a FishTopping?                                             | SUB      |
| 36 | Which topping would violate vegetarian restrictions if added to a MargheritaPizza?               | DISJ     |
| 37 | What cheese toppings are used in a FourCheesePizza?                                              | IND      |
| 38 | Which pizzas contain both OnionTopping and PepperTopping?                                        | PROP     |
| 39 | Is there a pizza with both HamTopping and MushroomTopping?                                       | PROP     |
| 40 | Which toppings are used in pizzas classified as SeafoodPizza?                                    | SUB      |
| 41 | Which pizza includes HotGreenPepperTopping?                                                      | IND      |
| 42 | Is there a pizza that is both spicy and contains seafood toppings?                               | LOGIC    |
| 43 | What pizzas are incompatible with CheeseTopping?                                                 | DISJ     |
| 44 | What are the ingredient constraints on a VegetarianHotPizza?                                     | LOGIC    |
| 45 | What pizza includes LeekTopping?                                                                 | IND      |
| 46 | Which pizzas are defined using exactly one topping?                                              | CARD     |
| 47 | What kinds of pizzas can have PineappleTopping?                                                  | PROP     |
| 48 | Which toppings are used on pizzas with a DeepPanBase?                                            | PROP     |
| 49 | Can a pizza be both ItalianPizza and AmericanPizza at the same time?                             | DISJ     |
| 50 | What is the cardinality restriction on toppings for a MargheritaPizza?                           | CARD     |
| 51 | Are MozzarellaTopping and GoatCheeseTopping disjoint?                                            | DISJ     |
| 52 | Which pizzas include SpicyBeefTopping?                                                           | PROP     |
| 53 | Which pizzas are defined with no meat toppings at all?                                           | LOGIC    |
| 54 | Which toppings would be illegal to add to a classified VegetarianPizza?                          | DISJ     |
| 55 | Are there any pizzas that include both TomatoTopping and LeekTopping?                            | PROP     |
| 56 | What type of pizzas include FishTopping but not CheeseTopping?                                   | LOGIC    |
| 57 | Which pizzas are classified as having spicy toppings only?                                       | LOGIC    |
| 58 | Is JalapenoTopping considered a HotTopping?                                                      | SUB      |
| 59 | What distinguishes a CheeseTopping from a VegetableTopping in the ontology?                      | SUB      |
| 60 | What pizzas use both ThinAndCrispyBase and a spicy topping?                                      | LOGIC    |



| Category Code | Reasoning Level                                | Description                                                   |
| ------------- | ---------------------------------------------- | ------------------------------------------------------------- |
| **IND**       | Individual-level fact                          | Uses asserted knowledge about named individuals               |
| **SUB**       | Subclass/Type hierarchy                        | Uses `subClassOf` or instance type inference                  |
| **PROP**      | Object/Data property usage                     | Uses `hasTopping`, `hasBase`, etc.                            |
| **DISJ**      | Disjointness and inconsistency checking        | Uses `disjointWith`, illegal combinations                     |
| **CARD**      | Cardinality restrictions                       | Uses OWL restrictions like `exactly`, `some`, `min`           |
| **LOGIC**     | Logical/semantic composition (complex queries) | Involves inference across multiple dimensions or conjunctions |
