# Optimizing the E-Commerce Experience: A fun project!
![image](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/e5aced8a-ddb6-414b-a0cd-7ba1d83fa725)

In today's shopping world, choices are like snacks at a party – plenty to pick from! If folks aren't loving what you're offering, they'll just hop to the next virtual aisle. To keep your customers in the groove, it's all about making them happy and keeping them loyal. Think of it like having a cool playlist for your online store!

Creating an e-commerce site isn't just about what customers need right now. It's about making them say, "Wow, this is my favorite store!" We want them to stick around like a catchy tune you can't get out of your head. So, let's make sure our online shop is the hit of the shopping charts! 🎶

#Website
![image](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/7ca48922-88f3-4a20-94bd-194943059c93)
![image](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/21581eb7-32c9-4c54-bfb0-78d462b6c2e7)

I made a website that's like Shopify to try some things out. You can find lots of easy guides on making your own online store. No need for tricky coding stuff! The main idea is to make the website work better for people – like a smoother ride for users. Let's keep it simple and fun! 🌟

The Website walkthrough is guided by walk me application which guides the user through various steps on the page. Again you can refer to tons of resources online to embed the walk-through logic. We will embed this at last after we analyze the pages that show a pattern of user's navigating throughout the website.

# Data Prep and Analyzing the Data
![Screen Shot 2024-01-13 at 1 07 11 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/15374363-08c2-4f93-87bc-dc36b5d0fad2)
![Screen Shot 2024-01-13 at 1 08 30 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/0897737f-bea4-4b1f-8091-243cb59e8a48)
![Screen Shot 2024-01-13 at 1 09 04 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/3fb8bea1-d00f-4629-9273-a178471ec97f)
›![Screen Shot 2024-01-13 at 1 09 25 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/31573aee-24bb-49e9-b4b7-af659397235e)
![Screen Shot 2024-01-13 at 1 10 20 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/058cbd5c-3884-44f2-8569-566655964e7c)
![Screen Shot 2024-01-13 at 1 10 47 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/b96a32cb-59bb-49e4-a0bf-f2196a855614)
Step 4 : Using Vlookup function assign the unique identifier values for each individual page. In my case---> 

=VLOOKUP(B2,$D$2:$E$324,2,false)
![Screen Shot 2024-01-13 at 1 11 40 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/390bac2f-c048-431d-9823-041fecefdfc9)

Step 5 : Transpose the values so that we obtain the p1,p2.. values for each user. 
![Screen Shot 2024-01-13 at 1 12 01 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/6e9e24ac-0a88-44ab-8e62-cacb4fb613b5)

# Machine Learning - Markov Chains
Markov process is a stochastic process that satisfies the Markov property of memory-lessness. A Markov chain is, in fact, a Markov process too in either discrete or continuous time with a countable state space.
![Screen Shot 2024-01-13 at 1 13 46 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/8dab8398-ced9-43f2-8016-8ad6718fef1c)
![Screen Shot 2024-01-13 at 1 14 05 AM](https://github.com/syedimad1998/Analyze_User_Workflow/assets/33065752/59a8016a-e141-4212-a60e-d16ccc39282c)

# Suggestion for UI/UX designer:

From the above transitional probabilities we can observe that :

Womens collection is more preferred but is not accessed from home page but from other pages which may result in a lengthy path for a user and we may lose the User, so hence we have to provide Womens collection offers at the home page inorder to increase sales.

Beats Headphones are purchased only from mens accessories but not from home page because of its less visibility between other products.These must be highlighted in order to sell this product.

Pashmina shaul product is a preferred product but due to its lack of visibility on the home page the sales are less.

Butterfly product image size must be reduced as it occupies large screen space.

Image resolution and other methods should be applied to increase the Website performance speed

On sale products must be featured on the top of the page rather on the footer as the featured products have been sold more than other products and this strategy may increase sales.

Sidebar can be implemented to display trending items and various offers to lure the customers into buying the product.

# Conclusion

However, all this analysis is worthless unless it is driving actions. Based on the above results a recurring process of reviewing must be initialized regarding web or application design and
