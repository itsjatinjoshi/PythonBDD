import logging as logger
import pdb;

def before_all(context):
    pdb.set_trace()
    logger.info("EXECUTE - BEFORE ALL")


def before_feature(context, feature):
    logger.info("EXECUTE -  BEFORE FEATURE")


def before_rule(context, rule):
    logger.info("EXECUTE -  BEFORE RULE")


def before_scenario(context, scenario):
    pdb.set_trace()
    logger.info("EXECUTE -  BEFORE SCENARIO")


def before_tag(context, tag):
    logger.info("EXECUTE -  BEFORE TAGS")


def before_step(context, step):
    logger.info("EXECUTE -  BEFORE STEPS")


# =============================================
def after_all(context):
    logger.info("EXECUTE - AFTER ALL")


def after_feature(context, feature):
    logger.info("EXECUTE -  AFTER FEATURE")


def after_rule(context, rule):
    logger.info("EXECUTE -  AFTER RULE")


def after_scenario(context, scenario):
    logger.info("EXECUTE -  AFTER SCENARIO")


def after_step(context, step):
    logger.info("EXECUTE -  AFTER STEP")


def after_tag(context, tag):
    logger.info("EXECUTE -  AFTER TAG")
