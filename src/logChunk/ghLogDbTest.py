import sys

sys.path.append("../util")
import Util
import unittest
import ghLogDb


class ghLogDbTest(unittest.TestCase):

    def setUp(self):
 
        Util.DATABASE = 0
        self.testCommit1 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit1.txt")
        self.testCommit2 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit2.txt")
        self.testCommit3 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit3.txt")
        self.testCommit4 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit4.txt")
        self.testCommit5 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit5.txt")
     
        self.testCommit7 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit7.txt")
        self.testCommit8 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit8.txt")
        self.testCommit9 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit9.txt")
        self.testCommit10 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit10.txt")
        self.testCommit11 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit11.txt")
        self.testCommit12 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit12.txt")
        #self.testCommit13 = ghLogDb.ghLogDb("testfiles/ghLogDbTest/TestCommit13.txt")

        self.testCommit1.processLog()
        self.testCommit2.processLog()
        self.testCommit3.processLog()
        self.testCommit4.processLog()
        self.testCommit5.processLog()
        self.testCommit7.processLog()
        self.testCommit8.processLog()
        self.testCommit9.processLog()
        self.testCommit10.processLog()
        self.testCommit11.processLog() #Make sure there is no crash
        self.testCommit12.processLog() #Make sure there is no crash
        #self.testCommit13.processLog() #Make sure there is no crash

        self.testCommitb1=ghLogDb.ghLogDb("testfiles/ghLogDbTestBlock/TestCommit1.txt")
        self.testCommitb1.processLog("../util/sample_conf2.ini")



 
    def test_Commit1(self):
        shas = self.testCommit1.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Liu Liu")
        patches = shas[0].patches
        self.assertTrue(len(patches) == 4)
        for patch in patches:
            self.assertTrue(patch.language == "c")
            self.assertTrue(patch.is_test == False)
            print(patch.file_name)

        self.assertTrue(patches[0].file_name == "bin/cuda/cwc-verify.c")
        methods = patches[0].methods
        self.assertTrue(len(methods) == 1) #Can't label stuff outside functions anymore unless we're looking for it.
        #self.assertTrue(methods[0].method == "NA")
        #self.assertTrue(methods[0].total_add == 1)
        #self.assertTrue(methods[0].total_del == 1)
        #testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        #self.assertEqual(testDict,methods[0].keywordDictionary)

        self.assertTrue(methods[0].method == "main")
        self.assertTrue(methods[0].total_add == 1)
        self.assertTrue(methods[0].total_del == 1)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)

        self.assertTrue(patches[1].file_name == "bin/image-net.c")
        methods = patches[1].methods
        self.assertTrue(len(methods) == 1)
        self.assertTrue(methods[0].method == "main")
        self.assertTrue(methods[0].total_add == 8)
        self.assertTrue(methods[0].total_del == 8)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)


        self.assertTrue(patches[2].file_name == "lib/ccv_convnet.c")
        methods = patches[2].methods
        self.assertTrue(len(methods)==6)
        self.assertTrue(methods[1].method == "ccv_convnet_verify")
        self.assertTrue(methods[1].total_add == 6)
        self.assertTrue(methods[1].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[1].keywordDictionary)
        self.assertTrue(patches[3].file_name == "lib/ccv_icf.c")
        methods = patches[3].methods
        self.assertTrue(len(methods)==1)

    def test_Commit2(self):
        shas = self.testCommit2.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Liu Liu")
        patches = shas[0].patches
        self.assertTrue(len(patches) == 2)
        for patch in patches:
            self.assertTrue(patch.language == "c")
            self.assertTrue(patch.is_test == False)
            print(patch.file_name)

        self.assertTrue(patches[0].file_name == "bin/cuda/cwc-bench.c")
        methods = patches[0].methods
        self.assertTrue(len(methods) == 1)
        self.assertTrue(methods[0].method == "main")
        self.assertTrue(methods[0].total_add == 43)
        self.assertTrue(methods[0].total_del == 5)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)



        self.assertTrue(patches[1].file_name == "bin/cuda/cwc-verify.c")
        methods = patches[1].methods

        self.assertTrue(len(methods) == 1)
        self.assertTrue(methods[0].method == "main")
        self.assertTrue(methods[0].total_add == 314)
        self.assertTrue(methods[0].total_del == 0)
        testDict = {'assert Adds':1, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)


    def test_Commit3(self):
        shas = self.testCommit3.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Liu Liu")
        patches = shas[0].patches
        self.assertTrue(len(patches) == 1)
        for patch in patches:
            self.assertTrue(patch.language == "c")
            self.assertTrue(patch.is_test == False)
            print(patch.file_name)

        self.assertTrue(patches[0].file_name == "lib/ccv_convnet.c")
        methods = patches[0].methods
        self.assertTrue(len(methods) == 2)


        self.assertTrue(methods[0].method == "_ccv_convnet_convolutional_forward_propagate_sse2")
        self.assertTrue(methods[0].total_add == 1)
        self.assertTrue(methods[0].total_del == 1)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)

        self.assertTrue(methods[1].method == "_ccv_convnet_convolutional_forward_propagate_neon")

        self.assertTrue(methods[1].total_add == 62)
        self.assertTrue(methods[1].total_del == 40)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[1].keywordDictionary)

    def test_Commit4(self):
        shas = self.testCommit4.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Liu Liu")
        patches = shas[0].patches
        self.assertTrue(len(patches) == 2)
        for patch in patches:
            self.assertTrue(patch.language == "c")
            self.assertTrue(patch.is_test == False)
            print(patch.file_name)

        methods = patches[0].methods
        self.assertTrue(len(methods) == 1)

        self.assertTrue(methods[0].method == "ccv_gemm")
        self.assertTrue(methods[0].total_add == 2)
        self.assertTrue(methods[0].total_del == 0)
        testDict = {'assert Adds':1, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)

        methods = patches[1].methods
        self.assertTrue(len(methods) == 2)
        self.assertTrue(methods[0].method == "_ccv_convnet_compute_softmax")
        self.assertTrue(methods[0].total_add == 0)
        self.assertTrue(methods[0].total_del == 18)
        testDict = {'assert Adds':0, 'assert Dels': 1, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)

        self.assertTrue(methods[1].method == "_ccv_convnet_compute_softmax")
        self.assertTrue(methods[1].total_add == 18)
        self.assertTrue(methods[1].total_del == 0)
        testDict = {'assert Adds':1, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)

    def test_Commit5(self):
        shas = self.testCommit5.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Lars Op den Kamp")
        patches = shas[0].patches
        self.assertTrue(len(patches) == 2)

        for patch in patches:
            self.assertTrue(patch.language == "cpp")
            self.assertTrue(patch.is_test == False)
            print(patch.file_name)

        methods = patches[0].methods
        self.assertTrue(len(methods) == 7)
        self.assertTrue(methods[3].method == "*dlopen")
        self.assertTrue(methods[3].total_add == 66)
        self.assertTrue(methods[3].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[3].keywordDictionary)

        methods = patches[1].methods
        self.assertTrue(len(methods) == 8)

    def test_Commit7(self):
        shas = self.testCommit7.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Dmitry Lenev")
        patches = shas[0].patches
        #print(patches)
        #patch[0].printPatch()
        self.assertTrue(len(patches) == 1)

        methods = patches[0].methods
        #print(len(methods))
        #print(methods)
        self.assertTrue(len(methods) == 9) #Should be 9, 7 minus the function deletion bug.

    def test_commit8(self):
        shas = self.testCommit8.shas
        self.assertTrue(len(shas) == 1)
        self.assertTrue(shas[0].author == "Sunny Bains")
        patches = shas[0].patches

        self.assertTrue(len(patches) == 1)

        methods = patches[0].methods
        self.assertTrue(len(methods) == 4)

        self.assertTrue(methods[0].method == "innobase_next_autoinc")
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_a Adds':9, 'ut_a Dels': 4, 'ut_ad Adds':0, 'ut_ad Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)

        self.assertTrue(methods[1].method == "ha_innobase::innobase_initialize_autoinc")
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[1].keywordDictionary)

        self.assertTrue(methods[2].method == "ha_innobase::update_row")
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[2].keywordDictionary)

        self.assertTrue(methods[3].method == "ha_innobase::get_auto_increment")
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[3].keywordDictionary)

    def test_commit9(self):
        shas = self.testCommit9.shas
        self.assertTrue(len(shas) == 1)
        #self.assertTrue(shas[0].author == "davi@mysql.com/endora.local") #It doesn't recognize this?
        patches = shas[0].patches

        self.assertTrue(len(patches) == 1)

        methods = patches[0].methods
        self.assertTrue(len(methods) == 10)

        self.assertTrue(methods[6].method == "mysql_stmt_close")
        testDict = {'assert Adds':1, 'assert Dels': 1, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[6].keywordDictionary)

    def test_commit10(self):
        shas = self.testCommit10.shas
        self.assertTrue(len(shas) == 1)
        self.assertTrue(shas[0].author == "Liu Liu")
        patches = shas[0].patches

        self.assertTrue(len(patches) == 5)

        methods = patches[3].methods
        self.assertTrue(len(methods) == 7)

        self.assertTrue(methods[0].method == "_ccv_read_rgb_raw")
        testDict = {'assert Adds':2, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,methods[0].keywordDictionary)

        methods = patches[4].methods
        self.assertTrue(len(methods) == 0) #Can't match the test case examples.


    # def setUp(self):
    #     self.testCommit1=ghLogDb.ghLogDb("test_case/TestCommit1.txt")
    #     self.testCommit1.processLog()
    #     self.testCommit2=ghLogDb.ghLogDb("test_case/TestCommit2.txt")
    #     self.testCommit2.processLog()


    def test_Commitb1(self):

        shas = self.testCommitb1.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Kevin Sawicki")
        patches = shas[0].patches
        self.assertTrue(len(patches) == 1)
        for patch in patches:
            self.assertTrue(patch.language == "java")
            self.assertTrue(patch.is_test == False)
            print(patch.file_name)

        self.assertTrue(patches[0].file_name == "app/src/main/java/com/github/mobile/accounts/AccountUtils.java")
        methods = patches[0].methods

        self.assertTrue(len(methods) == 1)
        self.assertTrue(methods[0].method == "getAccounts")
        self.assertTrue(methods[0].total_add == 1)
        self.assertTrue(methods[0].total_del == 2)
        dict= {'throw  Adds':0, 'catch Dels': 0, 'throw  Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}
        self.assertEqual(dict,methods[0].keywordDictionary)









if __name__=="__main__":
    unittest.main()