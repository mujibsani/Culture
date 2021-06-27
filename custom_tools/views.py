from django.shortcuts import render
from .forms import ArticleForm


def article(request):
    match_result = []
    match_count = list()
    non_match_results = []
    result_string = ""
    non_match_result_string = ""
    form = ArticleForm(request.POST)
    article_content = 'start'
    if form.is_valid():
        article_keywords = form.cleaned_data['give_your_keyword']
        article_content = form.cleaned_data['article']
        results = keyword_match(article_keywords, article_content)
        match_result = results.get('match')
        match_count = results.get('match_count')
        non_match_results = results.get('non_match')

    match_counter = 0
    for non_match in non_match_results:
        non_match_result_string += non_match + ', '
        # print(match_count[match_counter])

    for result in match_result:
        result_string += result + " " + match_count[match_counter] + ', '
        match_counter += 1
    # print(match_count)
    return render(request, 'tools/html/article.html',
                  {'form': form, 'results': result_string,
                   'non_match': non_match_result_string})


def keyword_match(keyword, article):
    match_result_list = []
    match_result_count = list()
    non_match_result = []
    keyword_array = keyword.split(',')
    for arr in keyword_array:
        if arr.lstrip() in article:
            match_result_list.append(arr.lstrip())
            match_result_count.append(keyword_number_count(arr.lstrip(), article))
        else:
            non_match_result.append(arr.lstrip())
    # match_result_dict = match_result_list.append(non_match_result)

    match_result_dict = {"match": match_result_list, "non_match": non_match_result, "match_count": match_result_count}
    return match_result_dict


def keyword_number_count(keyword, article):
    count = 0
    for i in range(len(article) - (len(keyword)-1)):
        new_article = article[i:]
        # print('new article :' + new_article)
        word = new_article[:len(keyword)]
        if keyword == word:
            count = count+1
            print(keyword)
    return str(count)
