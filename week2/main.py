from snowflake import Snowflake

if __name__ == '__main__':
    snow = Snowflake(7)
    snow.show()
    snow.thicken()
    snow.show()
    snow.thaw()
    snow.show()
    snow.freeze(2)
    snow.show()
