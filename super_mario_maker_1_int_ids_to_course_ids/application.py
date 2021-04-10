import logging
import struct
import hashlib
import hmac
import io

from super_mario_maker_1_int_ids_to_course_ids import model


MARIO_MAKER_MD5_KEY = hashlib.md5(b"9f2b4678").digest()

logger = logging.getLogger(__name__)

class Application:

    def run(self, parsed_args):

        result_set = set()

        with open(parsed_args.id_list, "r", encoding="utf-8") as f:

            line = None


            while True:

                line = f.readline()
                if not line:
                    logger.debug("bool(line) is False, breaking while loop")
                    break

                try:
                    result = self.convert_int_id_to_course_id(line.strip())

                    result_set.add(result)

                except Exception as e:
                    logger.exception("caught exception when trying to convert the line `%s` to a mario maker 1 course id", line)

                    continue

        sio = io.StringIO()

        first = True
        for iter_item in sorted(result_set, key=lambda x: x.integer_id):
            if first:
                first = False
            else:
                sio.write("\n")
            sio.write(f"{iter_item.as_course_id_str()}")

        sio.write("\n")

        logger.info("results: \n\n%s", sio.getvalue())

    def convert_int_id_to_course_id(self, int_id_str:str) -> model.MarioMakerOneCourseID:

        logger.debug("on integer id `%s`", int_id_str)

        int_id_as_int = int(int_id_str)

        # two is always hardcoded as 0000
        part_two = "0000"

        # the integer id we get is actually parts 3 and 4
        three_and_four_as_hex = "{:08X}".format(int_id_as_int)
        part_three = three_and_four_as_hex[:4]
        part_four = three_and_four_as_hex[4:]

        # calculate part one
        data = struct.pack("<Q", int_id_as_int)
        checksum = hmac.new(MARIO_MAKER_MD5_KEY, data, "md5").digest()
        part_one = checksum[3:1:-1].hex().upper()


        result = model.MarioMakerOneCourseID(
            integer_id=int_id_as_int,
            one=part_one,
            two=part_two,
            three=part_three,
            four=part_four)

        logger.debug("integer id `%s` returned result `%s`", int_id_str, result)

        return result