## Type
Talk

## Title
Django with MS SQL 
How can I do something awesome with Django if I work at a Microsoft Stack Shop? 

## Category
* You can use Django in the Microsoft Stack!
* Django with MS-SQL

## Elevator Pitch (300 Character Limit)
We all know how awesome Django is, but what do I do if I work in a Microsoft Shop where the Ops team can't stand up a Postgres Instance? With `mssql-django` you don't have to! You can use Django on Microsoft SQL Server and enjoy the benefits of Django (like the built in admin) in a Microsoft Shop.

## Audience
Django developers that work in a MS shop and want to use Django with a Legacy application while also developing new applications on with Django

## Audience Level
Intermediate Django experience


## Audience Takeaways
- Implementing Django with Legacy MS SQL databases
- UnManaged Tables can be your friend
- How to connect Django to multiple databases

## Outline
1. Motivation
	1. Why? Legacy Enterprise MS SQL Application (either vendor supplied or internal) 
2. Details
	1. packages needed
	2. Edge cases and sharp corners
3. Implementing
	1. Setting it up
	2. Using the Admin
4. Next Steps
	1. Creating custom APIs to interact with your legacy database


## Description
Slightly longer description. 
Expands upon elevator pitch. 
Be sure to include Audience Takeaways

We all know how awesome Django is, but what do I do if I work in a Microsoft Shop where the Ops team can't stand up a Postgres Instance? With `mssql-django` you don't have to! You can use Django on Microsoft SQL Server and enjoy the benefits of Django in a Microsoft Shop.

In this talk I'll go over a real(ish) world example of taking an existing MSSQL Database and adding Django. We'll see examples of implementing various views into non-managed models in the Admin section to allow users to update `configuration` tables. 

We'll also see how adding doc strings to the models created allow for a more maintainable set of configuration tables using the Admin Docs moduls of Django

`mssql-django` provides an enterprise database connectivity option for the Django Web Framework, with support for Microsoft SQL Server and Azure SQL Database and it's relevant because it allows all of us that may be working in a Microsoft Stack to use Django! 


## Internal Notes (For Your Eyes Only)
All the nitty gritty of the talk. 
Your scratch paper

## Additional Notes

Why am I talking about this? I work for a Healthcare company which is a Microsoft shop and I've been working with MSSQL for more than 10 years ... writing Stored Procedures, creating tables and views. I've written several Django sites as side projects and wanted to learn how to integrate something I love (Django) into my work so that my team and I can work with Django every day. 

---

    Do NOT start a talk with "if you've never heard of X before, it's basically ..."

    Much stronger to start with "X is ..., and it's relevant because ...".

    -> applies to everyone
    -> doesn't presume or dismiss knowledge
    -> starts on a positive note

From https://twitter.com/zooba/status/1524874382509744129



WHAT - How to integrate MSSQL into Django or how to get Django at your Microsoft Shop
WHY - many developers in a Microsoft Shop would like to use more Open-source software, but it's difficult to get buy-in from executives / managers. By showing that Django can integrate with the MS Stack that you may already have, showing how it can shorten some of the development time by using the Admin section 
HOW 

Review of `inspectdb` management command
Review of unmanaged tables
Review of multiple databases

WHO will benefit from your talk/tutorial (especially note concepts that attendees should be familiar with in order to get the most out of your presentation - ex: Models and/or Basic Database Design)