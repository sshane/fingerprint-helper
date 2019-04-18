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
                if len(make[model]) == 1:
                    match_dict[model] = {"matches": 0}
                    match_dict[model]["fingerprint"] = make[model][0]
                else:
                    match_dict[model + "_" + str(idx)] = {"matches": 0}
                    match_dict[model + "_" + str(idx)]["fingerprint"] = "multi"
                for key in fingerprint:
                    if key in unsupported_fp:
                        if fingerprint[key] == unsupported_fp[key]:
                            if len(make[model]) == 1:
                                match_dict[model]["matches"] += 1
                            else:
                                match_dict[model + "_" + str(idx)]["matches"] += 1
    
    match_sorted = OrderedDict(sorted(match_dict.items(), key=lambda x:x[1]['matches'], reverse=True))
    top_matches = [key for key in match_sorted.keys()][:5]
    for idx, top_match in enumerate(top_matches):
        if top_match[-2:-1] != "_":
            print(str(idx + 1) + ". " + top_match)
        else:
            print(str(idx + 1) + ". " + top_match[:-2] + " (fingerprint #" + str(int(top_match[-1:]) + 1) + ")")
        print("Exact matches: " + str(match_sorted[top_match]['matches']))
        if idx != 4:
            print()
    choice = int(input("Please enter the number next to the model you'd like to merge with: "))
    selected_model = match_sorted[top_matches[choice - 1]]
    if selected_model["fingerprint"] != "multi":
        merge_fingerprint(selected_model["fingerprint"], unsupported_fp)
    else:
        print("\nThe vehicle you selected has multiple fingerprints with code comments explaining which are which.\nPlease select the car from fingerprints.py and use merge_fingerprint() manually.")
    
    
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

    print("\nSucessfully merged!\n")
    if new_keys != 0:
        print(str(new_keys) + " new key/value pairs added to fingerprint!\n")
    if changed_keys != 0:
        print(str(changed_keys) + " changed key/value pairs!\n")
    print(model_fp)  # return new fingerprint merged with supplied unsupported fp
            
#find_matches({1:2, 4:3})
                
#merge_fingerprint({384: 8, 258: 8, 1031: 8, 264: 8, 268: 8, 653: 8, 270: 8, 280: 8, 274: 2, 660: 8, 792: 8, 284: 8, 669: 3, 671: 8, 544: 8, 290: 6, 291: 8, 292: 8, 294: 8, 168: 8, 559: 8, 520: 8, 308: 8, 564: 8, 571: 3, 320: 8, 800: 8, 324: 8, 331: 8, 332: 8, 288: 7, 760: 8, 514: 8, 344: 8, 770: 8, 672: 8, 863: 8, 736: 8, 737: 8, 746: 5, 658: 6, 368: 8, 625: 8, 500: 8, 501: 8, 680: 8, 532: 8, 764: 8},
#{68: 8, 168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 8, 660: 8, 669: 3, 671: 8, 672: 8, 680: 8, 701: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 746: 5, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 969: 4, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8})


#find_matches({55: 8, 181: 8, 256: 4, 257: 5, 258: 8, 264: 8, 268: 8, 272: 6, 273: 6, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 352: 8, 362: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 530: 8, 532: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 618: 8, 624: 8, 625: 8, 632: 8, 639: 8, 660: 8, 671: 8, 672: 8, 676: 8, 680: 8, 683: 8, 684: 8, 703: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 736: 8, 737: 8, 738: 8, 746: 5, 752: 2, 754: 8, 760: 8, 761: 8, 764: 8, 773: 8, 776: 8, 779: 8, 782: 8, 783: 8, 784: 8, 792: 8, 799: 8, 804: 8, 806: 2, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 831: 6, 832: 8, 838: 2, 844: 5, 848: 8, 853: 8, 856: 4, 860: 6, 882: 8, 897: 8, 906: 8, 924: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 968: 8, 969: 4, 970: 8, 973: 8, 974: 5, 977: 4, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1062: 8, 1098: 8, 1100: 8})