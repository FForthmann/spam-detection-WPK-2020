import logging
import csv
import time
from cap_features import cap_word_ratio, amount_cap_words, spammy_words, html_tag_count, not_spammy_words, numwords, \
    begin_with_re, spammy_phrases, count_exclamation_marks, square_bracket_count, has_html, num_link, has_gifs, has_jpg, \
    amount_capitalized_letters, numwords, words_containing_numbers_ratio, day_of_week


def main():
    base_path = "/Sandboxes/spam-detection-WPK-2020"
    logging.basicConfig(filename=base_path + 'log.log', level=logging.INFO)
    csv_value_index = 0
    csv_target_label_index = 1

    data_file_path = "spam_task_test.csv"

    features_csv_path = base_path + "features.csv"
    data_file_delimiter = "\t"
    omtArffName = "omt.arff"
    relationship_name = "@RELATION target"
    class_name = "@ATTRIBUTE TARGET {0, 1}"

    start = time.time()

    feature_functions = []

    # feature_functions.append(cap_word_ratio)
   # feature_functions.append(amount_cap_words)
    # feature_functions.append(html_tag_count)
    # feature_functions.append(begin_with_re)
    # feature_functions.append(count_exclamation_marks)
    feature_functions.append(square_bracket_count)
    # feature_functions.append(has_html)
   #feature_functions.append(num_link)
   # feature_functions.append(amount_capitalized_letters)
    # feature_functions.append(spammy_words)
    # feature_functions.append(not_spammy_words)
    # feature_functions.append(numwords)
    # feature_functions.append(spammy_phrases)
    # feature_functions.append(has_gifs)
    # feature_functions.append(has_jpg)
    # feature_functions.append(words_containing_numbers_ratio)
    # feature_functions.append(day_of_week)

    csv_reader = csv.reader(open(data_file_path, encoding='utf-8'), delimiter=data_file_delimiter)
    data_lines = [line for line in csv_reader]

    arff_lines = list()

    line_count = 1  # 0 is for the head
    for line in data_lines:

        print(str(line_count) + "    von        " + str(len(data_lines)))
        logging.info('    verarbeite Line Nr ' + str(line_count) + '    in ModularArffBuilder')
        logging.info('    lines total in modularArffBuilder: ' + str(len(data_lines)))
        num_feature = 0
        for feature in feature_functions:
            num_feature += 1
            data_text = line[csv_value_index]

            result_dict = feature(data_text)

            values = result_dict.get('values')
            heads = result_dict.get('heads')

            head_flag = False

            value_counter = 0
            for head in heads:
                if len(arff_lines) == 0:  # arff_lines has just been newly created
                    arff_lines.append([head])
                    arff_lines.append(
                        [values[value_counter]])  # first head arff_lines[0] and first value arff_lines[1] added
                    head_flag = True
                else:
                    if not head in arff_lines[0]:
                        arff_lines[0].append(head)  # feature has not yet been written in csv - append to head
                        arff_lines[line_count].append(
                            values[value_counter])  # since a new index needs to be added, also add value to the end
                        head_flag = True
                    else:
                        if (len(arff_lines) - 1) < line_count:
                            arff_lines.append([values[value_counter]])  # add new line to the end of arff_lines
                        else:
                            if (len(arff_lines[line_count]) - 1) < arff_lines[0].index(head):
                                arff_lines[line_count].append(
                                    values[value_counter])  # if head-index extends line indices, append.
                            else:
                                arff_lines[line_count][arff_lines[0].index(head)] = values[
                                    value_counter]  # fill the current line with values per head
                value_counter += 1

            if not head_flag:
                value_to_add = line[csv_target_label_index]
                arff_lines[line_count].append(value_to_add)
            else:
                if num_feature == len(feature_functions):
                    value_to_add = line[csv_target_label_index]
                    arff_lines[line_count].append(value_to_add)

        line_count += 1

    if not class_name in arff_lines[0]:
        class_name = class_name.replace("'", "")
        class_name = class_name.replace(",", "")
        arff_lines[0].extend([class_name])

    with open(features_csv_path, 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE, escapechar='\\')
        for line in arff_lines:
            writer.writerow(line)

            # now that the csv is done, we need to build the .arff file
    reader = csv.reader(open(features_csv_path))
    arff_lines = [line for line in reader]

    with open(base_path + omtArffName, "w") as arff:
        arff.write(relationship_name + "\n")
        for feature_head in arff_lines[0]:
            feature_head = feature_head.replace('[', '{')
            feature_head = feature_head.replace(']', '}')
            arff.write(feature_head.lstrip() + "\n")
        arff.write("@DATA\n")

        # leave out the first (head) line and write each line, separated by commas
        count_line = 0;
        for line_to_write in arff_lines:
            if count_line > 0:
                count_word = 0
                for word in line_to_write:
                    arff.write(word)
                    if (count_word + 1) < len(line_to_write):
                        arff.write(", ")
                    count_word += 1
                arff.write("\n")
            count_line += 1

    # monitor time taken to compute    
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
