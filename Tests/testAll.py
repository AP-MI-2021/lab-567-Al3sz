from Tests.testCRUD import testadaugarezervare, teststergerezervare, testmodificarezervare, testgetbyid
from Tests.testDomain import testRezervare
from Tests.testcerinte import testcerinta4, testcerinta5, testcerinta6economy, testcerinta6economyplus, \
    testcerinta6business, testcerinta7, testcerinta8
from Tests.testundoredo import testUndoRedo


def runAllTests():
    testRezervare()
    testadaugarezervare()
    teststergerezervare()
    testmodificarezervare()
    testgetbyid()
    testcerinta4()
    testcerinta5()
    testcerinta6economy()
    testcerinta6economyplus()
    testcerinta6business()
    testcerinta7()
    testcerinta8()
    testUndoRedo()