#coding: utf-8
season = ["April","Summer","Autum","Winter"]
itr_season = iter(season)
print type(itr_season)

print next(itr_season)

#for 
for i in itr_season:
	print i
