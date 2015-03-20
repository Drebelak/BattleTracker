__author__ = 'dylan'
import MySQLdb as MdB


def connect():
    return MdB.connect(host="engr-cpanel-mysql.engr.illinois.edu",
                       user="rebelak2_411ad",
                       passwd="cs411Battle",
                       db="rebelak2_battle_tracker")