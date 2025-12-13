def validateCoupons(code: list, businessLine: list, isActive: list) -> list:
    def is_valid(record: list):
        return (record[0] in valid_biz and record[2] and record[1].replace('_', 'a').isalnum())
    valid_biz = {'electronics', 'grocery', 'restaurant', 'pharmacy'}
    answer = sorted(filter(is_valid, zip(businessLine, code, isActive)))
    return [coup for _, coup, _ in answer]
