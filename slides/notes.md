

Question from @jackdlinke 

Absolutely! I'm a bit fan of Postgres, but it's not the only game in town and it certainly doesn't hurt to bring awareness to alternatives.

I see you recently forked a CFP proposal template. Both the template and the advice on Mason's blog are pretty solid. Finding something people aren't talking about (because it's new and they're unaware, or because it just hasn't been highlighted by anyone in the community) is a great approach. I did something similar for my talk last year, borrowing bits from various CFP examples I saw online and adapting it into my own. My template, bio, and CFPs (one accepted and one not accepted) are available at github.com/jacklinke/cfps/. I need to update them 😅

Having a template like that makes for a solid foundation for developing and submitting your CFP, and then it's easy to massage it for future conferences. Last year I gave a talk about using Django and htmx, and a few months later was asked to reprise that talk at another venue, and having the CFP outline and bio ready-to-go made it easy to update and provide details to the organizer for the second talk.

You seem pretty accomplished already, so I'm sure you'll have no problem putting something together on this topic. Do you want to approach it from a technical standpoint (you may not have known about using django and MSSQL together, here's why it hasn't been talked about, here's why you should use it), from a narrative approach (perhaps working through the process of developing a small project using MSSQL and discussing the benefits, pitfalls, and resources involved), or some other direction?

Once you have the idea a bit more fleshed out, let me know and I'll offer some feedback.

Have you done any public speaking before? You seem very accomplished, but I don't want to assume. Public speaking can be a challenge, but it's also very rewarding and worth pursuing. If you don't have much experience with this and your CFP gets accepted, I'd be happy review your talk beforehand - live or prerecorded and give some feedback.

Answer:

Thanks! 

I remember your talk from DjangoCon last year and thought it was 💯! I think we even chatted in the meeting space later that day with Jeff Triplet and Kojo Idrissa. 

The general idea is to use a project that I'm working on at my day job to introduce Django. We're a Microsoft shop which is why I'm interested in the Django-MSSQL combination. 

We have 3 internally developed web apps which have lots of configuration tables but no user interface for them. 

Anytime someone asks to have an item added to a drop down (or something similar) you have to dive into SQL Server Management Studio (SSMS) and make the update there. 

This is problematic for a few reasons, not least of which is that you need SSMS to make the update AND you need update permissions! This means that the less technical people on my team (or in the organization) that should be able to make the update can't. They have to submit a request to make the change to add an item. 

This can be even more complicated for the older legacy app where there's essentially no documentation on which table controls the drop down so you have to go dive into VB.Net code (which is in some cases a tangled mess of the worst kind of spaghetti code 😀 )

What I'd like to do is:

1. Show how to wire up Django to an existing MSSQL Database with multiple databases specified (https://docs.djangoproject.com/en/4.0/topics/db/multi-db/) using:
	* `mssql-django` library
	* unmanaged tables
2. Show how to keep the migrations contained to the database that they impact with database routers (https://docs.djangoproject.com/en/4.0/topics/db/multi-db/#database-routers)
3. Show examples of using the Django admin for these configuration tables
4. Show examples of including documentation on the Admin using the Django admin Docs generator (https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)

My two biggest concerns are:

1. Is this too much? 
2. Do I actually know what I'm doing well enough to present on it? 😂

In terms of public speaking I've done a bit of it. I once gave a talk at a conference in 2012 and dreaded every minute leading up to it. I tend to get very nervous before hand, but once I'm up talking I tend to settle in to a rhythm. That being said, if this does get accepted it would be awesome to get some feedback on it from you. 

Thanks again!


