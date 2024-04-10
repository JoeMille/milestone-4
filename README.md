# COSMIC COMMERCE

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Usage
As a prospective user of the Cosmic-Commerce application, I would like a seamless and interactive aesthetic that embodies the styles of generally enjoyable science fiction, whether it be browsing a catalog of futuristic legendary vehicles, others rendered from development description, armor and off planet gear, or simply viewing the constantly evolving particles JSON background and page turn animations. As a user I expect fast loading times, consistent feature design and the ability to explore products further, create an account and make mock purchases of said products within the catalog. Once my journey as a user is complete I would like to logout securely and feel confident my database data and user info is securely stored using the best principle available within the project confines.


## Project features 

# E-Commerce Platform Features

Cosmic-Commerce e-commerce platform is designed to provide a seamless shopping experience, with a futuristic aesthetic built using the principles of design amassed throughtout the four semesters of the Level 5 Developer course showcasing a true understanding of web development priciples;from browsing products, user auth, product management or simply making a purchase. Below are the main features implemented in this application.

## User Authentication and Registration

- **User Registration**: New users can sign up for an account using our registration form.
- **User Login and Logout**: Users can log in to access their accounts and log out when they're done.



## Product Catalog

- **Product Display**: Our homepage displays featured and legendary products, offering a quick glance at some of our top items.
- **Product Details**: Customers can view detailed information about a product by visiting the product detail page.
- **Category-based Browsing**: Products are organized by categories, making it easy for customers to browse items of interest.



## Shopping Basket

- **Adding Products to Basket**: Users can add products to their shopping basket, with the option to adjust quantities.
- **Basket Management**: Users can view, update, or remove items from their basket.
- **Checkout Process**: The checkout view allows users to review their basket items before proceeding with the purchase.


## Order and Payment

- **Checkout and Payment**: Integrated with Stripe for secure payment processing, allowing users to complete their purchase with ease.
- **Order Management**: After payment, an order record is created, detailing the purchased items and the user's information.

## Reviews

- **Writing Reviews**: Users can write reviews for products they've purchased, including ratings and comments.
- **Editing and Deleting Reviews**: Review authors have the option to edit or delete their reviews.

## Contact Form

- **Customer Feedback**: A contact form is available for users to send messages or feedback directly to the site administration.

## Additional Features

- Custom login view to redirect already authenticated users.
- Use of Django's built-in decorators for function-based views to require user authentication where necessary.
- Implementation of CSRF protection for form submissions.

This platform is built using Django, leveraging its powerful "batteries-included" features for web development and its secure, user-friendly authentication system.

#### Data-base management structure and overview

![DB Schematics](/readme-images/data-base-visual.png)

Cosmic-Commercep leverages a comprehensive database structure aimed at delivering an easy to manage user experience, efficient product management, and effective order processing. The following entities form the core of our sqlite3 database:

#### User
Represents the registered users of the platform. Inherits from Django's `AbstractUser` for immediate access to authentication functionalities. Includes attributes for usernames, passwords, email addresses, and profile details such as shipping addresses.

#### Group and Permission
These are part of Django's built-in authentication system, providing role-based permissions and access controls.

#### Basket and BasketItem
`Basket` is linked to a `User` and can contain multiple `BasketItem`s, which in turn are related to `Product`s. This setup manages the shopping basket features.

#### Product and Category
`Product` holds all details of the items for sale, including titles, descriptions, pricing, and images. Each product is associated with a `Category`, facilitating organized navigation and product browsing.

#### Order and CompletedOrder
Post-checkout, an `Order` record is generated capturing the purchase details, user information, and address. `CompletedOrder` may represent the finalized transaction records.

#### ContactMessage
Stores messages from the contact form, enabling user-administration communication.

#### Review
Allows users to post reviews on products with ratings and comments, fostering community interaction and product trustworthiness.

#### Session Management
Handled by `Session` and `AbstractBaseSession`, managing user sessions for secure and seamless user experiences.

#### LogEntry
Automatically records system changes, providing an audit trail for administrative actions.

This schema forms the backbone of our platform's database.

## Bugs and Resolutions

### Module Import Errors in Reviews App
**Issue:** While creating the reviews app, module import errors occurred due to conflicting application names and paths.
**Resolution:** Renamed the conflicting applications and adjusted the import paths accordingly. The `reviews` module definitions were rewritten and validated through isolated offline tests to ensure compatibility and functionality.

### Reviews Not Stored in Database
**Issue:** Naming conventions and model configurations were incorrect, which prevented reviews from being saved to the database.
**Resolution:** Reviewed and revised model field names and relationships to ensure data integrity and proper association between reviews and related entities. Conducted migrations to implement the updated models.

### Featured Products Styling
**Issue:** New 'Featured Products' functionality required specific styles that could not be inherited from parent elements.
**Resolution:** Implemented secondary styling dedicated to 'Featured Products', ensuring that the new functionality had a distinct and appealing visual presentation without inheriting unrelated styles.

### Admin Database Review Comments Not Captured
**Issue:** Review comments were not being captured or displayed in the admin database interface.
**Resolution:** Renamed the comment fields for clarity and reset the database migrations to reconcile schema discrepancies, restoring the functionality of review comments in the admin interface.

### Deployment Failure on Heroku
**Issue:** The project encountered a complete failure during the deployment process to Heroku due to incorrect file structure.
**Resolution:** Reorganized the file structure to meet Heroku's deployment requirements. Ensured all necessary configuration files were present and correctly set up for Heroku's build process.

### Incomplete requirements.txt File
**Issue:** The `requirements.txt` file was incomplete, requiring manual addition of each package due to not following the correct template.
**Resolution:** Regenerated `requirements.txt` using `pip freeze` to accurately capture the current environment's packages. Manually verified and added any missing dependencies to ensure a complete and accurate requirements file.

### Conflicting JavaScript Instances
**Issue:** Having two instances of particles animation on the loading wrapper caused JavaScript conflicts, preventing proper loading.
**Resolution:** Removed one instance of the particles animation and implemented a p5.js script to provide the intended visual effect. This allowed the preservation of the `particles.js` library functionality without causing conflicts.

### Stripe Payment Integration Errors
**Issue:** Users encountered errors with Stripe payment processing when entering card or user information.
**Resolution:** Investigated the Stripe integration setup to identify configuration or code errors. Ensured that API keys were correctly set and that the payment form was correctly handling user input. Tested the payment flow multiple times to ensure reliability and security.

## Installation

To install Cosmic-Commerce as a template for future project simply navigate to https://github.com/JoeMille/milestone-4, copying the root URL and cloning within your projects terminal. This will download the full Django project available for further customisation. Cloning this project will require user to create their own personal API secret keys for Stripe which until completing will render payment function use impossible. Once your project is prooperly installed and ensuring that manage.py and related files are at the root directory of your project, open a terminal and input the command: python3 manage.py runserver. This will render your project to the browser for devlopment view. 

Once the cloned project is ready for deployment, list all project requirements within a requirements.txt file at the root directory, inputting the command: pip3 install -r requirements.txt. Once completed, create a new Heroku application by navigating to your Heroku dashboard and creating a new application. Finally, commit all staged changes to your git repository and input the terminal command: git push heroku main. Wait whilst heroku uploads all changes to the hosted application and once successfully deployed, navigate to your heroku dashboard and launch your newly compiled application. 


## Summary

MS4 (Mileston-Project-4) proved to be the most difficult of all combined projects as it required embodying all elements learned and practiced throughout the last three modules, often times pushing development back to refresh knowledge of the priciples of each module. A personal mountain to hike was anything javascript related, at first I not only, admittedly, feared the language but also avoided it's use. This is a humongous regret in hindsight as it has now become the most interesting and versatile language I have yet been exposed to. Trying to highlight my huge appreciation of the language this project utilises open source javascript libraries that bear the weight of the "interactive-sci-fi" aesthetic as well as the sites payment model. In the future I hope to continue to expand my understanding of all modules content and truly hope that Cosmic-Commerce is a firm representation of what can be learned via the SDC/CI syllabus and what features and personality I can personally bring to the project table. I hope this project is an enjoyable perusal, especially for fans of some of the "Techy/Trekky" choices made throughout. 

Kindest of thanks for reading and exploring, and please feel free to follow this account for future releases and projects as well as view my personal progression through past projects. 

"End Session". 


## License

## Contact



## Acknowledgements



## Additional Sections (Optional)

- Troubleshooting
- FAQs
- Changelog
- Roadmap
- Credits
- etc.

