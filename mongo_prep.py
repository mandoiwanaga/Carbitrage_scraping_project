def prep_lists_for_mongo(titles,years,prices,mileages):
    """
    Takes lists of scraping results for:
        titles, prices, and mileages
    and transforms into list of dictionaries
    Returns: list of dictionaries; each dict has one auto result
    """
    n = len(titles)
    autos = []
    for i in range(n):
        autos.append({'title':titles[i]
                      ,'year':years[i]
                      ,'price':prices[i]
                      ,'miles':mileages[i]
                     })

    return autos