import ast
import fingerprints
from collections import OrderedDict

makes = [fingerprints.TOYOTA_FINGERPRINTS, fingerprints.GM_FINGERPRINTS, fingerprints.FORD_FINGERPRINTS, fingerprints.HONDA_FINGERPRINTS, fingerprints.CHRYSLER_FINGERPRINTS, fingerprints.HYUNDAI_FINGERPRINTS]

def find_matches(unsupported_fp=""):
    if unsupported_fp == "":
        unsupported_fp = input("Enter fingerprint: ")
    if type(unsupported_fp) == str:  # formatting for from sentry
        unsupported_fp = unsupported_fp.replace("L:", ":")
        unsupported_fp = ast.literal_eval(unsupported_fp)
    match_dict = {}
    #makes = [{"Corolla": [{1:2, 4:3}]}]
    for make in makes:
        for model in make:
            for idx, fingerprint in enumerate(make[model]):
                if fingerprint == unsupported_fp and len(fingerprint) == len(unsupported_fp):  # if exact fingerprint match
                    print("Exact fingerprint match!")
                    print(model)
                    return
                if len(make[model]) == 1:
                    match_dict[model] = {"matches": 0, "mismatches": 0}
                    match_dict[model]["fingerprint"] = make[model][idx]
                else:
                    match_dict[model + "_" + str(idx)] = {"matches": 0, "mismatches": 0}
                    match_dict[model + "_" + str(idx)]["fingerprint"] = make[model][idx]
                for key in fingerprint:
                    if key in unsupported_fp:
                        if fingerprint[key] == unsupported_fp[key]:
                            if len(make[model]) == 1:
                                match_dict[model]["matches"] += 1
                            else:
                                match_dict[model + "_" + str(idx)]["matches"] += 1
                        else:
                            if len(make[model]) == 1:
                                match_dict[model]["mismatches"] += 1
                            else:
                                match_dict[model + "_" + str(idx)]["mismatches"] += 1
    
    match_sorted = OrderedDict(sorted(match_dict.items(), key=lambda x:x[1]['matches'], reverse=True))
    top_matches = [key for key in match_sorted.keys()][:5]
    for idx, top_match in enumerate(top_matches):
        if top_match[-2:-1] != "_":
            print(str(idx + 1) + ". " + top_match)
        else:
            print(str(idx + 1) + ". " + top_match[:-2] + " (fingerprint #" + str(int(top_match[-1:]) + 1) + ")")
        print("Exact matches: " + str(match_sorted[top_match]['matches']))
        if match_dict[top_match]['mismatches'] != 0:
            print(str(match_dict[top_match]['mismatches']) + " mismatches")
        else:
            print("No mismatches")
        if abs(len(unsupported_fp) - len(match_dict[top_match]['fingerprint'])) != 0:
            if len(unsupported_fp) > len(match_dict[top_match]['fingerprint']):
                print(str(abs(len(unsupported_fp) - len(match_dict[top_match]['fingerprint']))) + " new key/value pairs")
            else:
                print(str(abs(len(unsupported_fp) - len(match_dict[top_match]['fingerprint']))) + " less key/value pairs")
        if idx != 4:
            print()
    choice = int(input("Please enter the number next to the model you'd like to merge with: "))
    selected_model = match_dict[top_matches[choice - 1]]['fingerprint']
    #if selected_model["fingerprint"] != "multi":
    print()
    merge_fingerprint(selected_model, unsupported_fp)
    #else:
        #print("\nThe vehicle you selected has multiple fingerprints with code comments explaining which are which.\nPlease select the car from fingerprints.py and use merge_fingerprint() manually.")
    
    
def merge_fingerprint(model_fp, unsupported_fp):  # current, supported fingerprint in openpilot and unsupported fingerprint from sentry error (in dict type)
    mismatches = []
    for key in unsupported_fp:
        if key in model_fp:
            if unsupported_fp[key] != model_fp[key]:
                mismatches.append(key)
    
    if len(mismatches) != 0:
        mismatch_text = "mismatch" if len(mismatches) == 1 else "mismatches"
        print(str(len(mismatches)) + " value " + mismatch_text + " to fix!\n")
        new_values = {}
        for mismatch in mismatches:
            print("Key: " + str(mismatch))
            print("Your unsupported fingerprint value: " + str(unsupported_fp[mismatch]))
            print("Selected model fingerprint value: " + str(model_fp[mismatch]))
            new_values[mismatch] = int(input("Please type value to use with merge: "))
    
    new_keys = 0
    changed_keys = 0
    for key in unsupported_fp:
        if key not in model_fp:  # add new key/value pair to model fingerprint
            new_keys += 1
            model_fp[key] = unsupported_fp[key]
        elif unsupported_fp[key] != model_fp[key]:  # if value in unsupported fp doesn't match one in model fp, use user chosen value above
            changed_keys += 1
            model_fp[key] = new_values[key]
    if new_keys == 0 and changed_keys == 0:
        print("Nothing to add/change.")
    else:
        print("\nSucessfully merged!\n")
    if new_keys != 0:
        print(str(new_keys) + " new key/value pairs added to fingerprint!\n")
    if changed_keys != 0:
        print(str(changed_keys) + " changed key/value pairs!\n")
    print(model_fp)  # return new fingerprint merged with supplied unsupported fp

                
#merge_fingerprint({384: 8, 258: 8, 1031: 8, 264: 8, 268: 8, 653: 8, 270: 8, 280: 8, 274: 2, 660: 8, 792: 8, 284: 8, 669: 3, 671: 8, 544: 8, 290: 6, 291: 8, 292: 8, 294: 8, 168: 8, 559: 8, 520: 8, 308: 8, 564: 8, 571: 3, 320: 8, 800: 8, 324: 8, 331: 8, 332: 8, 288: 7, 760: 8, 514: 8, 344: 8, 770: 8, 672: 8, 863: 8, 736: 8, 737: 8, 746: 5, 658: 6, 368: 8, 625: 8, 500: 8, 501: 8, 680: 8, 532: 8, 764: 8},
#{68: 8, 168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 8, 660: 8, 669: 3, 671: 8, 672: 8, 680: 8, 701: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 746: 5, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 969: 4, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8})


find_matches("{1552L: 8, 1553L: 8, 1554L: 8, 1043L: 8, 1561L: 8, 1568L: 8, 1569L: 8, 1570L: 8, 1059L: 1, 36L: 8, 37L: 8, 550L: 8, 552L: 4, 560L: 7, 1589L: 8, 1592L: 8, 1593L: 8, 1595L: 8, 1599L: 8, 581L: 5, 1112L: 8, 1114L: 8, 608L: 8, 610L: 5, 1041L: 8, 1656L: 8, 643L: 7, 1176L: 8, 1177L: 8, 1178L: 8, 1179L: 8, 1180L: 8, 1181L: 8, 1184L: 8, 1185L: 8, 1186L: 8, 1189L: 8, 1190L: 8, 1191L: 8, 1192L: 8, 170L: 8, 1196L: 8, 1197L: 8, 1198L: 8, 1199L: 8, 180L: 8, 1206L: 8, 1212L: 8, 1728L: 8, 1056L: 8, 713L: 8, 1232L: 8, 1745L: 8, 1571L: 8, 1237L: 8, 1572L: 8, 1263L: 8, 979L: 2, 800L: 8, 1584L: 8, 296L: 8, 835L: 8, 836L: 8, 849L: 4, 869L: 7, 870L: 7, 896L: 8, 905L: 8, 911L: 8, 916L: 3, 918L: 7, 921L: 8, 933L: 8, 426L: 6, 944L: 8, 945L: 8, 1779L: 8, 950L: 8, 951L: 8, 953L: 3, 955L: 8, 956L: 8, 452L: 8, 466L: 8, 467L: 8, 1014L: 8, 1017L: 8, 1020L: 8}")