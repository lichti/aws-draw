import pprint
import aws_draw

draw = aws_draw.config()
pprint.pprint(draw.aws_accounts)
aws_draw.D2(draw.aws_accounts)
