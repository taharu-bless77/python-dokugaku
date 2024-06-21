def format_yen_with_commas(yen):
    # str.format() を使って3桁ごとにコンマで区切るフォーマット
    formatted_string = "{:,}".format(yen)
    return formatted_string