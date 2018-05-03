# SommelAI



### Steven Jiang and Tony DiPadova 

## Goals

Wine is viewed as a sophisticated beverage, only to be understood by the wine connoisseurs of the upper class. When ordering wine at an upscale restaurant, it is not uncommon to ask for recommendations from the waiter. We are interested in making the understanding of wine more accessible to the general public. Through exploring a wine dataset with features such as ratings, variety, region of origin, and description, we can determine the extent to which price and quality vary by region of origin. Additionally, the dataset incorporates textual descriptions of the wine. Ideally, we would like to tokenize and parse the descriptions to extract vectorized word counts to predict price and quality based on textual descriptive factors. Finally, it is generally assumed that higher priced wines are also better in quality. Although the data is inherently biased because the wine ratings are not from a blind taste test, it would still be interesting to determine the extent to which price and quality are correlated.

## Dataset
We are interested in using the Kaggle Wine Reviews dataset (https://www.kaggle.com/zynicide/wine-reviews/data). The dataset is composed of ~150,000 unique wine reviews and contains the following fields: country, description, designation, points, price, province, region\_1, region\_2, variety, and winery. Country, province, region\_1, and region\_2 refer to the various degrees of specificity regarding location of origin of the wine. Winery refers to the winery that made the wine and designation refers to the vineyard within the winery from which the grapes used to make the wine come. The description field includes a description from a sommelier about the wine’s taste, smell, look, feel, etc. Finally, the variety field refers to the types of grapes used to produce the wine. Using the aforementioned features, we hope to predict points, which is a proxy for quality, and price.

## Questions
* Do price and quality vary by region, variety, or winery? If so, to what extent?
* Can textual descriptions provided by sommeliers be used to predict wine price and quality?
* Are price and quality correlated?


