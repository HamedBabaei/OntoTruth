| Q# | Question                                                                                         | Category |
| -- | ------------------------------------------------------------------------------------------------ | -------- |
| 1  | What are the common toppings of a Margherita Pizza?                                              | IND      |MozzarellaTopping, TomatoTopping |MargheritaPizza has hasTopping some (MozzarellaTopping and TomatoTopping).
| 2  | Is a FourCheesePizza considered a VegetarianPizza?                                               | SUB      |Yes. FourCheesesTopping is a topping used in QuattroFormaggi, this query can go to logic(complex reasoning)
| 3  | What toppings make a pizza classified as a HotAndSpicyPizza?                                     | SUB      |HotGreenPepperTopping, HotSpicedBeefTopping, JalapenoPepperTopping, TobascoPepperSauce — anything with hasSpiciness value hot.
| 4  | Which pizzas contain both MushroomTopping and MozzarellaTopping?                                 | PROP     |Mushroom, LaReine, Giardiniera, FourSeasons.
| 5  | Can a pizza have both HamTopping and AnchovyTopping without violating any disjoint restrictions? | DISJ     |No. Disjointness exists between MeatTopping and FishTopping.
| 6  | What makes a pizza incompatible with a ThinAndCrispyBase?                                        | DISJ     |DeepPanBase is disjoint with ThinAndCrispyBase.
| 7  | What topping is classified as both spicy and vegetarian?                                         | LOGIC    |JalapenoPepperTopping, HotGreenPepperTopping, CajunSpiceTopping, TobascoPepperSauce
| 8  | Which pizzas are defined to contain exactly two toppings?                                        | CARD     |MargheritaPizza has exactly two toppings: MozzarellaTopping, TomatoTopping. (Consider using hasTopping max 2)
| 9  | Are there any pizzas that are both AmericanPizza and VegetarianPizza?                            | SUB      |No. Uses hasValue restriction on different individuals.
| 10 | Which toppings are disjoint with CheeseTopping?                                                  | DISJ     |VegetableTopping, MeatTopping, FishTopping, HerbSpiceTopping, FruitTopping, NutTopping, SauceToppin
| 11 | Is a QuattroFormaggiPizza classified as a CheesePizza?                                           | SUB      |Yes. QuattroFormaggiPizza has topping FourCheesesTopping.
| 12 | What toppings are used in a SloppyGiuseppePizza?                                                 | IND      |HotSpicedBeefTopping, MozzarellaTopping, TomatoTopping, OnionTopping, GreenPepperTopping
| 13 | What distinguishes a VegetarianPizza from a NonVegetarianPizza?                                  | SUB      |FishTopping and MeatTopping |Nonveg toppings are Fish Meat and vegetarian pizza doesnt have these
| 14 | Which pizzas are defined to have a DeepPanBase?                                                  | PROP     |None explicitly. Only class DeepPanBase exists. Consider removing it
| 15 | What type of base is used in a SoHoPizza?                                                        | IND      |Not specified. Consider removing it
| 16 | Can a pizza have both PrawnTopping and ChickenTopping?                                           | DISJ     |No. Disjointness between FishTopping (e.g., PrawnTopping) and MeatTopping (e.g., ChickenTopping).Similar Query (no. 5) Above. Should we keep only 1?
| 17 | What is the minimum number of toppings on a SupremePizza?                                        | CARD     |Not defined in ontology.| Consider removing it
| 18 | Is a VenezianaPizza suitable for vegetarians?                                                    | SUB      |Yes
| 19 | What spicy meat topping is commonly found on American-style pizzas?                              | IND      |PeperoniSausageTopping (spiciness: Medium)
| 20 | Which pizzas include OliveTopping as one of their ingredients?                                   | PROP     |Capricciosa, Fiorentina, FourSeasones, Giardiniera, Napoletana, Soho, Veneziana, Siciliana, LaReine.
| 21 | Are there any pizzas defined to be both HotAndSpicy and Vegetarian?                              | SUB      |None|  Only non-vegetarian pizzas are defined as HotAndSpicyPizza.
| 22 | What kind of topping is RocketTopping categorized as?                                            | SUB      |VegetableTopping. RocketTopping subclassOf VegetableTopping (spiciness: Medium)
| 23 | Can a pizza be both a SeafoodPizza and a VegetarianPizza?                                        | DISJ     |No (FishTopping is disjoint with VegetarianPizza).
| 24 | What are the common toppings on a NapolitanaPizza?                                               | IND      |AnchoviesTopping, MozzarellaTopping, TomatoTopping, CaperTopping, OliveTopping
| 25 | What is the difference between a TomatoTopping and a SundriedTomatoTopping?                      | SUB      |SundriedTomatoTopping is a subclass of TomatoTopping.
| 26 | What toppings are considered disjoint from MeatTopping?                                          | DISJ     |VegetableTopping, CheeseTopping, FishTopping, HerbSpiceTopping, FruitTopping, NutTopping, SauceTopping| Repeated
| 27 | What class of pizza does an AmericanHotPizza belong to?                                          | SUB      |NamedPizza; also subclass of CheesyPizza, InterestingPizza, MeatyPizza, SpicyPizzaEquivalent
| 28 | Can a pizza have more than one type of cheese topping?                                           | CARD     |Yes (e.g., QuattroFormaggi uses FourCheesesTopping).
| 29 | Which pizzas are built using a ThinAndCrispyBase?                                                | PROP     |RealItalianPizza, Napoletana, Veneziana
| 30 | Is there a pizza that includes both CaperTopping and AnchovyTopping?                             | PROP     |Yes (e.g., Capricciosa, FourSeasons).
| 31 | Which pizzas use GarlicTopping as an ingredient?                                                 | PROP     |Fiorentina, FruttiDiMare, PolloAdAstra, Soho, Siciliana
| 32 | What toppings are only allowed on a VegetarianPizza?                                             | DISJ     |None. 
| 33 | Is ArtichokeTopping considered a vegetable topping?                                              | SUB      |Yes (subclass of VegetableTopping).
| 34 | Which pizzas contain more than three toppings?                                                   | CARD     |SloppyGiuseppe, Parmense,Veneziana,VegetarianPizzaEquivalent, Soho, AmericanHot,PolloAdAstra,PrinceCarlo, Siciliana, Cajun, Capricciosa, Caprina, Napoletana,Fiorentina, FourSeasons, Giardiniera, LaReine,
| 35 | What distinguishes a MeatTopping from a FishTopping?                                             | SUB      |Spiciness. MeatTopping and FishTopping are disjoint.
| 36 | Which topping would violate vegetarian restrictions if added to a MargheritaPizza?               | DISJ     |Any MeatTopping  or FishTopping.
| 37 | What cheese toppings are used in a FourCheesePizza?                                              | IND      |Not explicitly in ontology. Possibly refers to FourCheesesTopping.
| 38 | Which pizzas contain both OnionTopping and PepperTopping?                                        | PROP     |PolloAdAstra, SloppyGiuseppe, Cajun, 
| 39 | Is there a pizza with both HamTopping and MushroomTopping?                                       | PROP     |Yes (LaReine).
| 40 | Which toppings are used in pizzas classified as SeafoodPizza?                                    | SUB      |No SeafoodPizza class defined. But toppings may include FishTopping (AnchoviesTopping, PrawnTopping)
| 41 | Which pizza includes HotGreenPepperTopping?                                                      | IND      |AmericanHot
| 42 | Is there a pizza that is both spicy and contains seafood toppings?                               | LOGIC    |No. Pizzas like AmericanHotPizza, CajunPizza are spicy but meat-based.
| 43 | What pizzas are incompatible with CheeseTopping?                                                 | DISJ     |FruttiDiMare
| 44 | What are the ingredient constraints on a VegetarianHotPizza?                                     | LOGIC    |Not defined (class VegetarianHotPizza doesn’t exist).
| 45 | What pizza includes LeekTopping?                                                                 | IND      |PrinceCarlo, Giardiniera
| 46 | Which pizzas are defined using exactly one topping?                                              | CARD     |None. All have at least two toppings. MargheritaPizza sometimes has only one.
| 47 | What kinds of pizzas can have PineappleTopping?                                                  | PROP     |Not mentioned in ontology. Remove?
| 48 | Which toppings are used on pizzas with a DeepPanBase?                                            | PROP     |Not specified. Remove?
| 49 | Can a pizza be both ItalianPizza and AmericanPizza at the same time?                             | DISJ     |No. ItalianPizza and AmericanPizza have hasCountryOfOrigin values {Italy} and {America}, which are distinct individuals.
| 50 | What is the cardinality restriction on toppings for a MargheritaPizza?                           | CARD     |Max 2 Toppings(MozzarellaTopping + TomatoTopping).
| 51 | Are MozzarellaTopping and GoatCheeseTopping disjoint?                                            | DISJ     |Yes (explicitly disjoint).
| 52 | Which pizzas include SpicyBeefTopping?                                                           | PROP     |SloppyGiuseppe (HotSpicedBeefTopping).
| 53 | Which pizzas are defined with no meat toppings at all?                                           | LOGIC    |VegetarianPizza (e.g., Margherita, QuattroFormaggi).
| 54 | Which toppings would be illegal to add to a classified VegetarianPizza?                          | DISJ     |MeatTopping (e.g., HamTopping), FishTopping (e.g., AnchoviesTopping).
| 55 | Are there any pizzas that include both TomatoTopping and LeekTopping?                            | PROP     |Giardiniera, PrinceCarlo.
| 56 | What type of pizzas include FishTopping but not CheeseTopping?                                   | LOGIC    |FruttiDiMare (as it explicitly doesnt mention any cheesetopping).
| 57 | Which pizzas are classified as having spicy toppings only?                                       | LOGIC    |None (all have mild/medium, other toppings too).
| 58 | Is JalapenoTopping considered a HotTopping?                                                      | SUB      |HotTopping not declared explicitly but we may get a few answers like Jalapeno using hasTopping some (hasSpiciness Hot).
| 59 | What distinguishes a CheeseTopping from a VegetableTopping in the ontology?                      | SUB      |Disjoint classes . Different subclasses
| 60 | What pizzas use both ThinAndCrispyBase and a spicy topping?                                      | LOGIC    |RealItalianPizza is a pizza with italian origin, veneziana is a RealitalianPizza and has Onion topping which is medium spicy.



| Category Code | Reasoning Level                                | Description                                                   |
| ------------- | ---------------------------------------------- | ------------------------------------------------------------- |
| **IND**       | Individual-level fact                          | Uses asserted knowledge about named individuals               |Can be removed
| **SUB**       | Subclass/Type hierarchy                        | Uses `subClassOf` or instance type inference                  |
| **PROP**      | Object/Data property usage                     | Uses `hasTopping`, `hasBase`, etc.                            |
| **DISJ**      | Disjointness and inconsistency checking        | Uses `disjointWith`, illegal combinations                     |
| **CARD**      | Cardinality restrictions                       | Uses OWL restrictions like `exactly`, `some`, `min`           |
| **LOGIC**     | Logical/semantic composition (complex queries) | Involves inference across multiple dimensions or conjunctions | cn be renamed as complex queries
