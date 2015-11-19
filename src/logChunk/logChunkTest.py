import unittest
import logChunk

class logChunktest(unittest.TestCase):

    def readHelper(self,filename):
        inf =open(filename,"r")
        text=""
        for line in inf:
            text+=line

        return text


    def debugFunctions(self, funcList):
        print("===========================================")
        for func in funcList:
            print(func.method)
            print(func.start)
            print(func.end)
            print(func.total_add)
            print(func.total_del)
            print(func.keywordDictionary)           
        print("===========================================")


    def setUp(self):
        self.keyword1 = ["wtc/Assertions.h","excluded","single"]
        self.keyword2 = ["ut_ad","included","single"]
        self.keyword3 = ["try","Included","BLOCK"]
        self.keyword4 = ["for","excludeD","block"]
        self.keyword5 = ["ut_ad included single"]
        self.keyword6 = ["printf(format","str)","included","single"]
        self.keyword7 = ["printf(format, str)","included","single"]
        self.keyword8 = ["assert","incuded","single"]
        self.keyword9 = ["assert","included","lock"]


        self.method1 = "static void blarg() {"
        self.method2 = "int more(int stuff) {"
        self.method3 = "ccv_string * getStuff (int[] stuffToGet) {"
        self.method4 = "int add2to3(int (*functionPtr)(int, int)) {"
        self.method5 = "public static void other(int one, int (*functionPtr)(int, int) {"
        self.method6 = "static void\n multiline(\n int arg1, string arg2\n) {"
        self.method7 = "int lotsOfSpace     (int stuff) {"
        self.method8 = "                .matrix = {"
        self.method9 = "ccv_string* getStuff (int[] stuffToGet) {"
        self.method10 = "ccv_string *getStuff (int[] stuffToGet) {"
        self.method11 = "void NdbBlob::getBlobEvent(NdbEventImpl& be, const NdbEventImpl* e, const NdbColumnImpl* c) {"
        self.method12 = "bool Repair_mrg_table_error_handler::handle_condition(THD *,uint sql_errno,const char*, MYSQL_ERROR::enum_warning_level level,const char*,MYSQL_ERROR ** cond_hdl) {"
        self.method13 = "(_log2) += 1;  static int CeilingLog2(unsigned int i) {"
        #self.method14 = "(STATEMENT_CONSTRUCTOR_BASE_PARAMETERS, ExpressionPtr exp)   : Statement(STATEMENT_CONSTRUCTOR_BASE_PARAMETER_VALUES),     m_exp(exp) {"
        self.method15 = "static JSC::UString& globalExceptionString(){"
        self.method16 = "(jint) AWT_WINDOW_LOST_FOCUS, (jint) AWT_WINDOW_DEACTIVATED,  static gboolean window_focus_in_cb (GtkWidget * widget, GdkEventFocus *event, jobject peer) {"
        self.method17 = "LinuxPtraceDumper dumper(getpid()); }  TEST(LinuxPtraceDumperTest, FindMappings) {"

        self.testChunk = logChunk.logChunk("")
        #Read in the single tests
        self.chunk1 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk1.txt")) #Check
        self.chunk2 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk2.txt")) #Check
        self.chunk3 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk3.txt")) #Check
        #self.chunk4 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk4.txt")) #Nope
        #self.chunk5 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk5.txt")) #Nope
        self.chunk6 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk6.txt")) #Check
        self.chunk7 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk7.txt")) #Check
        self.chunk8 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk8.txt")) #Check
        self.chunk9 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk9.txt")) #Check
        self.chunk10 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk10.txt")) #Check
        self.chunk11 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk11.txt")) #Check
        self.chunk12 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk12.txt")) #Check
        self.chunk13 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk13.txt")) #Check
        self.chunk14 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk14.txt")) #Check
        self.chunk15 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk15.txt")) #Check
        #self.chunk16 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk16.txt")) #Nope
        #self.chunk17 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk17.txt")) #Nope
        #self.chunk18 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk18.txt")) #Nope
        #self.chunk19 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk19.txt")) #Nope
        #self.chunk20 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk20.txt")) #Nope
        self.chunk21 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk21.txt")) #Check
        self.chunk22 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk22.txt")) #Check
        self.chunk23 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk23.txt")) #Check
        self.chunk24 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk24.txt")) #Check
        self.chunk25 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk25.txt")) #Check
        #self.chunk26 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk26.txt")) #Nope
        self.chunk27 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk27.txt")) #Check
        #self.chunk28 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk28.txt")) #Nope
        self.chunk29 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk29.txt")) #Check
        #self.chunk30 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk30.txt")) #Maybe?
        self.chunk31 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk31.txt")) #Check
        self.chunk32 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk32.txt")) #Check
        self.chunk33 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk33.txt")) #Check
        #self.chunk34 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk34.txt")) #Nope
        self.chunk35 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk35.txt")) #Check
        self.chunk36 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk36.txt")) #Check
        self.chunk37 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk37.txt")) #Check
        self.chunk38 = logChunk.logChunk(self.readHelper("testfiles/Single/testChunk38.txt")) #Check

        #Read in the block tests
        self.chunkb1 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk1.txt"),"sample_conf2.ini")
        self.chunkb2 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk2.txt"),"sample_conf2.ini")
        self.chunkb3 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk3.txt"),"sample_conf2.ini")
        self.chunkb4 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk4.txt"),"sample_conf2.ini")
        self.chunkb5 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk5.txt"),"sample_conf2.ini")
        self.chunkb6 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk6.txt"),"sample_conf2.ini")
        self.chunkb7 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk7.txt"),"sample_conf2.ini")
        self.chunkb8 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk8.txt"),"sample_conf2.ini")
        self.chunkb9 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk9.txt"),"sample_conf2.ini")
        self.chunkb10 = logChunk.logChunk(self.readHelper("testfiles/Block/testChunk10.txt"),"sample_conf2.ini")



    def test_KeywordValidityCheck(self):
        self.assertTrue(self.testChunk.keywordValidityCheck(self.keyword1))
        self.assertTrue(self.testChunk.keywordValidityCheck(self.keyword2))
        self.assertTrue(self.testChunk.keywordValidityCheck(self.keyword3))
        self.assertTrue(self.testChunk.keywordValidityCheck(self.keyword4))
        self.assertFalse(self.testChunk.keywordValidityCheck(self.keyword5))
        self.assertFalse(self.testChunk.keywordValidityCheck(self.keyword6))
        self.assertTrue(self.testChunk.keywordValidityCheck(self.keyword7))
        self.assertFalse(self.testChunk.keywordValidityCheck(self.keyword8))
        self.assertFalse(self.testChunk.keywordValidityCheck(self.keyword9))


    def test_FunctionNameParse(self):
        temp = self.testChunk.parseFunctionName(self.method1)
        self.assertTrue(temp == "blarg", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method2)
        self.assertTrue(temp == "more", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method3)
        self.assertTrue(temp == "getStuff", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method4)
        self.assertTrue(temp == "add2to3", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method5)
        self.assertTrue(temp == "other", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method6)
        self.assertTrue(temp == "multiline", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method7)
        self.assertTrue(temp == "lotsOfSpace", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method8)
        self.assertTrue(temp == "", "Actual: " + temp)

        temp = self.testChunk.parseFunctionName(self.method13)
        self.assertTrue(temp == "CeilingLog2", "Actual: " + temp)
        #print(self.testChunk.getFunctionPattern(self.method14))
        #temp = self.testChunk.parseFunctionName(self.testChunk.getFunctionPattern(self.method14))
        #self.assertTrue(temp == "m_exp", "Actual: " + temp)
        temp = self.testChunk.parseFunctionName(self.method16)
        self.assertTrue(temp == "window_focus_in_cb", "Actual: " + temp)

    def test_AssignPattern(self):
        self.assertTrue(self.testChunk.isAssignment(".matrix = {"))
        self.assertTrue(self.testChunk.isAssignment(".blah ={"))
        self.assertFalse(self.testChunk.isAssignment("realFunction(int default = 0) {"))

    def test_isClassDef(self):
        self.assertTrue(self.testChunk.isClassDef("class A {"))
        self.assertTrue(self.testChunk.isClassDef("template <class T> class calc {"))
        self.assertTrue(self.testChunk.isClassDef("template <class T> class calc : public superclass {"))
        self.assertFalse(self.testChunk.isClassDef("template <class T> T mypair<T>::getmax () {"))
        self.assertFalse(self.testChunk.isClassDef("template < class T > T mypair<T>::getmax () {"))
        self.assertFalse(self.testChunk.isClassDef("Class *cls = *clsh;       while (cls) {"))
        self.assertTrue(self.testChunk.isClassDef("static MDL_global_lock global_lock;  class MDL_object_lock : public MDL_lock {"))

    def test_isConstructorOrDestructor(self):
        self.assertTrue(self.testChunk.isConstructorOrDestructor("~StackHelper() {", "stackhelper"))
        self.assertTrue(self.testChunk.isConstructorOrDestructor("WindowProperties(GdkRectangle* geometry, bool toolbarVisible, bool statusbarVisible, bool scrollbarsVisible, bool menubarVisible,                          bool locationbarVisible, bool resizable, bool fullscreen)             : m_isNull(false)             , m_geometry(*geometry)             , m_toolbarVisible(toolbarVisible)             , m_statusbarVisible(statusbarVisible)             , m_scrollbarsVisible(scrollbarsVisible)             , m_menubarVisible(menubarVisible)             , m_locationbarVisible(locationbarVisible)             , m_resizable(resizable)             , m_fullscreen(fullscreen)         {","windowproperties"))
        self.assertTrue(self.testChunk.isConstructorOrDestructorWithList("      UIClientTest()         : m_scriptDialogType(WEBKIT_SCRIPT_DIALOG_ALERT)         , m_scriptDialogConfirmed(true)         , m_allowPermissionRequests(false)         , m_mouseTargetModifiers(0)     {", ["uiclienttest","windowproperties"]))

    def test_isFunction(self):
        self.assertTrue(self.testChunk.isFunction(self.method1))
        self.assertTrue(self.testChunk.isFunction(self.method2))
        self.assertTrue(self.testChunk.isFunction(self.method3))
        self.assertTrue(self.testChunk.isFunction(self.method4))
        self.assertTrue(self.testChunk.isFunction(self.method5))
        self.assertTrue(self.testChunk.isFunction(self.method6))
        self.assertTrue(self.testChunk.isFunction(self.method7))
        self.assertFalse(self.testChunk.isFunction(self.method8))
        self.assertTrue(self.testChunk.isFunction(self.method9))
        self.assertTrue(self.testChunk.isFunction(self.method10))
        self.assertTrue(self.testChunk.isFunction(self.method11))
        self.assertTrue(self.testChunk.isFunction(self.method12))
        self.assertFalse(self.testChunk.isFunction("class Repair_mrg_table_error_handler : public Internal_error_handler{"))
        self.assertFalse(self.testChunk.isFunction("while(1) {"))
        self.assertFalse(self.testChunk.isFunction("else if(1) {"))
        self.assertTrue(self.testChunk.isFunction(self.method13))
        #self.assertFalse(self.testChunk.isFunction(self.method14))
        self.assertTrue(self.testChunk.isFunction(self.method15))
        self.assertTrue(self.testChunk.isFunction(self.method16))
        # self.assertFalse(self.testChunk.isFunction(self.method17))

    def test_parseText_Single1(self):
        self.chunk1.parseText()
        funcList = self.chunk1.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 3) #Should be no mock function for asserts
        self.assertTrue(funcList[0].method=="NdbBlob::getBlobEventName")
        self.assertTrue(funcList[0].total_add == 10)
        self.assertTrue(funcList[0].total_del == 0)

        testDict = {'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 0, 'ut_a Dels': 0}

        self.assertEqual(testDict,funcList[0].keywordDictionary)

        self.assertTrue(funcList[1].method=="NdbBlob::getBlobEventName")
        self.assertTrue(funcList[1].start==19)
        self.assertTrue(funcList[1].end==22)
        self.assertTrue(funcList[1].total_add == 4)
        self.assertTrue(funcList[1].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[1].keywordDictionary)


        self.assertTrue(funcList[2].method=="NdbBlob::getBlobEvent")
        self.assertTrue(funcList[2].start==26)
        self.assertTrue(funcList[2].end==60)
        self.assertTrue(funcList[2].total_add == 35)
        self.assertTrue(funcList[2].total_del == 0)
        testDict = {'assert Adds':2, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[2].keywordDictionary)

    def test_parseText_Single2(self):
        self.chunk2.parseText()
        funcList = self.chunk2.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 1)

        self.assertTrue(funcList[0].method=="btr_pcur_release_leaf")
        self.assertTrue(funcList[0].start==0)
        self.assertTrue(funcList[0].end==0)
        self.assertTrue(funcList[0].total_add == 0)
        self.assertTrue(funcList[0].total_del == 0)

        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 1, 'ut_a Adds':0, 'ut_a Dels': 2}
        self.assertEqual(testDict,funcList[0].keywordDictionary)

    def test_parseText_Single3(self):
        self.chunk3.parseText()
        funcList = self.chunk3.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 3)
        self.assertTrue(funcList[0].method=="m_unhandled_errors") #This is wrong, but I'm not sure how to fix it.
        self.assertTrue(funcList[0].start==13)
        self.assertTrue(funcList[0].end==13)
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 0)

        testDict = {'assert Adds':1, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[0].keywordDictionary)

        self.assertTrue(funcList[1].method=="safely_trapped_errors")
        self.assertTrue(funcList[1].start==27)
        self.assertTrue(funcList[1].end==42)

        self.assertTrue(funcList[1].total_add == 16)
        self.assertTrue(funcList[1].total_del == 0)

        testDict = {'assert Adds':1, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[1].keywordDictionary)


        self.assertTrue(funcList[2].method=="Repair_mrg_table_error_handler::handle_condition")
        self.assertTrue(funcList[2].start==57)
        self.assertTrue(funcList[2].end==67)
        self.assertTrue(funcList[2].total_add == 11)
        self.assertTrue(funcList[2].total_del == 0)

        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[2].keywordDictionary)

    def test_parseText_Single6(self):
        self.chunk6.parseText()
        funcList = self.chunk6.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 3)
        self.assertTrue(funcList[0].method ==  "calc<A_Type>::multiply")
        self.assertTrue(funcList[0].start == 8)
        self.assertTrue(funcList[0].end == 10)
        self.assertTrue(funcList[0].total_add == 3)
        self.assertTrue(funcList[0].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[0].keywordDictionary)


        self.assertTrue(funcList[1].method ==  "calc<A_Type>::add")
        self.assertTrue(funcList[1].start == 12)
        self.assertTrue(funcList[1].end == 14)
        self.assertTrue(funcList[1].total_add == 3)
        self.assertTrue(funcList[1].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[1].keywordDictionary)


        self.assertTrue(funcList[2].method ==  "calc<A_Type>::divide")
        self.assertTrue(funcList[2].start == 16)
        self.assertTrue(funcList[2].end == 19)
        self.assertTrue(funcList[2].total_add == 4)
        self.assertTrue(funcList[2].total_del == 0)
        testDict = {'assert Adds':1, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[2].keywordDictionary)

    def test_parseText_Single7(self):
        self.chunk7.parseText()
        funcList = self.chunk7.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 15) #Should be 17, but can't find constructor/destructor outside of class
        self.assertTrue(funcList[6].method ==  "CDVDDemuxPVRClient::Abort", "Actual: " + funcList[7].method)

    def test_parseText_Single8(self):
        self.chunk8.parseText()
        funcList = self.chunk8.functions
        self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 4)

        self.assertTrue(funcList[0].method ==  "GetHelperBinary")
        self.assertTrue(funcList[0].start == 62)
        self.assertTrue(funcList[0].end == 77)
        self.assertTrue(funcList[0].total_add == 16)
        self.assertTrue(funcList[0].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[0].keywordDictionary)

        self.assertTrue(funcList[1].method ==  "StackHelper")
        self.assertTrue(funcList[1].start == 113)
        self.assertTrue(funcList[1].end == 113)
        self.assertTrue(funcList[1].total_add == 1)
        self.assertTrue(funcList[1].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[1].keywordDictionary)

        self.assertTrue(funcList[2].method ==  "~StackHelper")
        self.assertTrue(funcList[2].start == 114)
        self.assertTrue(funcList[2].end == 117)
        self.assertTrue(funcList[2].total_add == 4)
        self.assertTrue(funcList[2].total_del == 0)
        testDict = {'assert Adds':0, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[2].keywordDictionary)

        self.assertTrue(funcList[3].method ==  "NO_FUNC_CONTEXT")
        self.assertTrue(funcList[3].start == 0)
        self.assertTrue(funcList[3].end == 0)
        self.assertTrue(funcList[3].total_add == 0)
        self.assertTrue(funcList[3].total_del == 0)
        testDict = {'assert Adds':32, 'assert Dels': 0, 'ut_ad Adds':0, 'ut_ad Dels': 0, 'ut_a Adds':0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[3].keywordDictionary)

    def test_parseText_Single9(self):
        self.chunk9.parseText()

        funcList = self.chunk9.functions
        # self.debugFunctions(funcList)
        #Can't find constructors or destructors outside of classes
        self.assertTrue(len(funcList) == 19)

        self.assertTrue(funcList[6].method ==  "CRuntimeMethod")
        self.assertTrue(funcList[6].start == 119)
        self.assertTrue(funcList[6].end == 121)
        self.assertTrue(funcList[6].total_add == 3)
        self.assertTrue(funcList[6].total_del == 0)
        testDict = { 'ut_ad Adds': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Dels': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[6].keywordDictionary)

    def test_parseText_Single10(self):
        self.chunk10.parseText()
        funcList = self.chunk10.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 6)

        self.assertTrue(funcList[3].method ==  "FreeArenaList")
        self.assertTrue(funcList[3].start == 203)
        self.assertTrue(funcList[3].end == 246)
        self.assertTrue(funcList[3].total_add == 44)
        self.assertTrue(funcList[3].total_del == 0)
        testDict = { 'ut_ad Adds': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Dels': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[3].keywordDictionary)

    def test_parseText_Single11(self):
        self.chunk11.parseText()
        funcList = self.chunk11.functions
        self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 5)

        self.assertTrue(funcList[4].method ==  "parseArgs")
        self.assertTrue(funcList[4].start == 81)
        self.assertTrue(funcList[4].end == 199)
        self.assertTrue(funcList[4].total_add == 118)
        self.assertTrue(funcList[4].total_del == 0)
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[4].keywordDictionary)

    def test_parseText_Single12(self):
        self.chunk12.parseText()
        funcList = self.chunk12.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 3)

        self.assertTrue(funcList[1].method ==  "mbfl_buffer_converter_delete")
        self.assertTrue(funcList[1].start == 173)
        self.assertTrue(funcList[1].end == 184)
        self.assertTrue(funcList[1].total_add == 12)
        self.assertTrue(funcList[1].total_del == 0)
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 0, 'ut_a Dels': 0}
        self.assertEqual(testDict,funcList[1].keywordDictionary)

    def test_parseText_Single13(self):
        self.chunk13.parseText() #Broken like 2 is
        funcList = self.chunk13.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 2)

        self.assertTrue(funcList[0].method ==  "ClassCache::hashKey")
        self.assertTrue(funcList[0].start == 6)
        self.assertTrue(funcList[0].end == 8)
        self.assertTrue(funcList[0].total_add == 0)
        self.assertTrue(funcList[0].total_del == 3)
        self.assertTrue(len(funcList[0].assertionList) == 0)

        self.assertTrue(funcList[1].method ==  "ClassCache::lookup")
        self.assertTrue(funcList[1].start == 13)
        self.assertTrue(funcList[1].end == 41)
        self.assertTrue(funcList[1].total_add == 0)
        self.assertTrue(funcList[1].total_del == 29)
        self.assertTrue(len(funcList[1].assertionList) == 0)

    def test_parseText_Single14(self):
        self.chunk14.parseText()
        funcList = self.chunk14.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 1)

        self.assertTrue(funcList[0].method ==  "getDynLocType")
        self.assertTrue(funcList[0].start == 8)
        self.assertTrue(funcList[0].end == 241)

        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 15, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[0].keywordDictionary)

    def test_parseText_Single15(self):
        self.chunk15.parseText()
        # funcList = self.chunk15.functions
        # #self.debugFunctions(funcList)

    def test_parseText_Single21(self):
        self.chunk21.parseText()
        funcList = self.chunk21.functions
        #self.debugFunctions(funcList)

        self.assertTrue(len(funcList) == 1)
        self.assertTrue(funcList[0].method ==  "MDL_object_lock")

    def test_parseText_Single22(self):
        self.chunk22.parseText()
        funcList = self.chunk22.functions
        #self.debugFunctions(funcList)

        self.assertTrue(len(funcList) == 6) #Can't get the last one b/c constructor out of context
        self.assertTrue(funcList[0].method ==  "MDL_map::init")
        self.assertTrue(funcList[1].method ==  "MDL_map::destroy")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[0].keywordDictionary)

        self.assertTrue(funcList[2].method ==  "MDL_map::find_or_insert")
        self.assertTrue(funcList[3].method ==  "MDL_map::find")
        self.assertTrue(funcList[4].method ==  "MDL_map::move_from_hash_to_lock_mutex")

        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 2, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[4].keywordDictionary)
        self.assertTrue(funcList[5].method ==  "MDL_map::remove")

        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[5].keywordDictionary)

    def test_parseText_Single23(self):
        self.chunk23.parseText()
        funcList = self.chunk23.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 2)

        #Broken like 2...
        self.assertTrue(funcList[0].method ==  "MDL_ticket::has_pending_conflicting_lock_impl")
        self.assertTrue(len(funcList[0].assertionList) == 2)
        self.assertTrue(funcList[1].method ==  "MDL_ticket::has_pending_conflicting_lock") #Name not in + or -
        self.assertTrue(len(funcList[1].assertionList) == 1)

    def test_parseText_Single24(self):
        self.chunk24.parseText()
        funcList = self.chunk24.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 24)

        self.assertTrue(funcList[16].method ==  "*get_date_time_format_str")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[16].keywordDictionary)

    def test_parseText_Single25(self):
        self.chunk25.parseText()
        funcList = self.chunk25.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 4)

        self.assertTrue(funcList[2].method ==  "row_upd_index_replace_new_col_vals_index_pos")
        testDict = { 'ut_ad Adds': 1, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 1, 'assert Adds': 0, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[2].keywordDictionary)

    def test_parseText_Single27(self):
        self.chunk27.parseText()
        funcList = self.chunk27.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 30)

    def test_parseText_Single29(self):
        self.chunk29.parseText()
        funcList = self.chunk29.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 15)

        self.assertTrue(funcList[11].method ==  "sfmt_fill_array32")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 3, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[11].keywordDictionary)

        self.assertTrue(funcList[12].method ==  "sfmt_fill_array64")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 3, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[12].keywordDictionary)

    def test_parseText_Single31(self):
        self.chunk31.parseText() #Broken like 2 is
        # BROKEN LIKE 2
        funcList = self.chunk31.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 2)

        self.assertTrue(funcList[0].method ==  "smp_callin")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[0].keywordDictionary)

        self.assertTrue(funcList[1].method ==  "NO_FUNC_CONTEXT")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[1].keywordDictionary)

    def test_parseText_Single32(self):
        self.chunk32.parseText()
        funcList = self.chunk32.functions
        # #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 10)

        self.assertTrue(funcList[1].method ==  "h264_er_decode_mb")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[1].keywordDictionary)


        self.assertTrue(funcList[7].method ==  "alloc_picture")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 2, 'ut_a Dels': 0}
        self.assertTrue(testDict,funcList[7].keywordDictionary)

    def test_parseText_Single33(self):
        self.chunk33.parseText()
        #Problems:
        #Also, get a false assert when we have a function name named assert.
        funcList = self.chunk33.functions
        #self.debugFunctions(funcList)
        # print("Length: " + str(len(funcList)))
        self.assertTrue(len(funcList) == 23)

    def test_parseText_Single35(self):
        self.chunk35.parseText()
        funcList = self.chunk35.functions
        #self.debugFunctions(funcList)

        for func in funcList:
            self.assertFalse(func.method ==  "NO_FUNC_CONTEXT")

    def test_parseText_Single36(self):
        self.chunk36.parseText() #Broken like 2 is
        #BROKEN LIKE 2
        funcList = self.chunk36.functions
        #self.debugFunctions(funcList)

        self.assertTrue(len(funcList) == 3) # 2 + 1 Mock

        self.assertTrue(funcList[1].method ==  "Patch")
        self.assertTrue(len(funcList[1].assertionList) == 5)

        self.assertTrue(funcList[2].method ==  "NO_FUNC_CONTEXT")
        self.assertTrue(len(funcList[2].assertionList) == 1)

    def test_parseText_Single37(self):
        self.chunk37.parseText()
        funcList = self.chunk37.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 1)
        self.assertTrue(funcList[0].method ==  "NamespaceDetails::_alloc")
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 1, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict, funcList[0].keywordDictionary)

    def test_parseText_Single38(self):
        self.chunk38.parseText()
        funcList = self.chunk38.functions
        #self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 5)
        self.assertTrue(funcList[0].method == "mysql_stmt_fetch")
        self.assertTrue(funcList[0].total_add == 6)
        self.assertTrue(funcList[0].total_del == 1)
        self.assertTrue(funcList[1].method ==  "mysql_stmt_reset")
        self.assertTrue(funcList[1].total_add == 6)
        self.assertTrue(funcList[1].total_del == 1)
        testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 1, 'ut_a Dels': 0}
        self.assertTrue(testDict, funcList[1].keywordDictionary)

    def test_parseText_Block1(self):

        self.chunkb1.parseText()
        funcList = self.chunkb1.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 2) #Should be no mock function for asserts
        self.assertTrue(self.chunkb1.bracketMisMatch==0)

        self.assertTrue(funcList[0].method=="foo")
        self.assertTrue(funcList[0].total_add == 2)
        self.assertTrue(funcList[0].total_del == 1)
        dict= {'throw  Adds': 0, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 1, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 1, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}


        self.assertEqual(dict,funcList[0].keywordDictionary)
        self.assertTrue(funcList[1].method=="foo00022")
        self.assertTrue(funcList[1].total_add == 4)
        self.assertTrue(funcList[1].total_del == 2)
        dict= {'throw  Adds': 0, 'catch Dels': 0, 'try Adds': 1, 'try Dels': 1, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 1, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}

        self.assertEqual(dict,funcList[1].keywordDictionary)

    def test_parseText_Block2(self):

        self.chunkb2.parseText()
        funcList = self.chunkb2.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 2) #Should be no mock function for asserts
        self.assertTrue(self.chunkb2.bracketMisMatch==0)

        self.assertTrue(funcList[0].method=="getAccounts")
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 2)
        dict= {'throw  Adds': 0, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}




        self.assertEqual(dict,funcList[0].keywordDictionary)

        self.assertTrue(funcList[1].method=="getAccount")
        self.assertTrue(funcList[1].total_add == 6)
        self.assertTrue(funcList[1].total_del == 2)
        dict={'throw  Adds': 1, 'catch Dels': 0, 'try Adds': 2, 'try Dels': 2, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 4, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 2, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}


        self.assertEqual(dict,funcList[1].keywordDictionary)


    def test_parseText_Block3(self):

        self.chunkb3.parseText()
        funcList = self.chunkb3.functions

        # self.debugFunctions(funcList)

        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunkb3.bracketMisMatch==0)

        self.assertTrue(funcList[0].method=="ReflectiveProperty")
        self.assertTrue(funcList[0].total_add == 12)
        self.assertTrue(funcList[0].total_del == 3)
        dict= {'throw  Adds': 0, 'catch Dels': 1, 'try Adds': 8, 'try Dels': 2, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 4, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}

        self.assertEqual(dict,funcList[0].keywordDictionary)

    def test_parseText_Block4(self):

        self.chunkb4.parseText()
        funcList = self.chunkb4.functions
        # self.debugFunctions(funcList)


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        # self.assertTrue(self.chunkb4.isExceptionChunkFlag==0)
        self.assertTrue(self.chunkb4.bracketMisMatch==0)

        self.assertTrue(funcList[0].method=="setHandle")
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 1)
        dict= {'throw  Adds': 0, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}
        self.assertEqual(dict,funcList[0].keywordDictionary)

    def test_parseText_Block5(self):

        self.chunkb5.parseText()
        funcList = self.chunkb5.functions
        # self.debugFunctions(funcList)


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunkb5.bracketMisMatch==0)
        self.assertTrue(funcList[0].method=="copy")
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 5)

        dict= {'throw  Adds': 0, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 1, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 1, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}

        self.assertEqual(dict,funcList[0].keywordDictionary)


    def test_parseText_Block6(self):

        self.chunkb6.parseText()
        funcList = self.chunkb6.functions
        # self.debugFunctions(funcList)


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunkb5.bracketMisMatch==0)

        self.assertTrue(funcList[0].method=="init")
        self.assertTrue(funcList[0].total_add == 0)
        self.assertTrue(funcList[0].total_del == 1)
        dict= {'throw  Adds': 0, 'catch Dels': 1, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 1, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 1, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}

        self.assertEqual(dict,funcList[0].keywordDictionary)


    def test_parseText_Block7(self):

        self.chunkb7.parseText()
        funcList = self.chunkb7.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunkb7.bracketMisMatch==0)
        self.assertTrue(funcList[0].method=="onCreateLoader")
        self.assertTrue(funcList[0].total_add == 2)
        self.assertTrue(funcList[0].total_del == 7)
        #TODO for Dels should be 0. FIXME
        dict= {'throw  Adds': 0, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 1, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 1, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}

        self.assertEqual(dict,funcList[0].keywordDictionary)


    def test_parseText_Block8(self):

        self.chunkb8.parseText()
        funcList = self.chunkb8.functions
        # self.debugFunctions(funcList)

        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunkb8.bracketMisMatch==0)
        self.assertTrue(funcList[0].method=="getAuthToken")
        self.assertTrue(funcList[0].total_add == 2)
        self.assertTrue(funcList[0].total_del == 2)
        dict= {'throw  Adds': 1, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 1, 'exception Dels': 1, 'raise Adds': 0, 'catch Adds': 2, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 2, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}
        self.assertEqual(dict,funcList[0].keywordDictionary)


    def test_parseText_Block9(self):

        self.chunkb9.parseText()
        funcList = self.chunkb9.functions
        # self.debugFunctions(funcList)


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunkb9.bracketMisMatch==0)


        self.assertTrue(funcList[0].method=="getAuthToken")
        self.assertTrue(funcList[0].total_add == 2)
        self.assertTrue(funcList[0].total_del == 2)
        dict= {'throw  Adds': 1, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 1, 'raise Adds': 0, 'catch Adds': 2, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 2, 'raise Dels': 0, 'for Adds': 0,'for Dels': 0,'while Adds': 0,'while Dels': 0}

        self.assertEqual(dict,funcList[0].keywordDictionary)


    def test_parseText_Block10(self):

        self.chunkb10.parseText()
        funcList = self.chunkb10.functions
        # self.debugFunctions(funcList)
        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunkb10.bracketMisMatch==0)


        self.assertTrue(funcList[0].method=="getToken")
        self.assertTrue(funcList[0].total_add == 8)
        self.assertTrue(funcList[0].total_del == 3)
        dict= {'throw  Adds': 0, 'catch Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'throw  Dels': 0, 'exception Adds': 0, 'raise Dels': 0, 'for Adds': 4,'for Dels': 2,'while Adds': 3,'while Dels': 1}

        self.assertEqual(dict,funcList[0].keywordDictionary)




#This olds test cases that no longer apply under the new spec
    #def test_parseText_SingleNA(self):
        # #self.chunk4.parseText()
        # #self.chunk5.parseText()
        # #self.chunk16.parseText()
        # #self.chunk17.parseText()
        # #self.chunk18.parseText()
        # #self.chunk19.parseText()
        # #self.chunk20.parseText()
        # #self.chunk26.parseText()
        # #self.chunk28.parseText()
        # #self.chunk30.parseText()
        # #self.chunk34.parseText()

        # funcList = self.chunk4.functions
        # #self.debugFunctions(funcList)
        # self.assertTrue(len(funcList) == 0)

        # funcList = self.chunk5.functions
        # #self.debugFunctions(funcList)
        # self.assertTrue(len(funcList) == 0)
        # self.assertTrue(self.chunk5.total_add == 20)
        # self.assertTrue(self.chunk5.total_del == 1)

        # funcList = self.chunk16.functions
        # #self.debugFunctions(funcList)

        # funcList = self.chunk17.functions
        # #self.debugFunctions(funcList)

        # funcList = self.chunk18.functions
        # #self.debugFunctions(funcList)

        # #Bug: Can't see a return type, but at least this no longer crashes.
        # #self.assertTrue(len(funcList) == 1)
        # #self.assertTrue(funcList[0].method ==  "build_call_n")

        # funcList = self.chunk19.functions
        # #self.debugFunctions(funcList)
        # #print("FUNCTIONS")
        # #print(funcList)
        # self.assertTrue(len(funcList) == 2)

        # self.assertTrue(funcList[0].method ==  "window_focus_in_cb")

        # self.assertTrue(funcList[1].method ==  "window_focus_out_cb")
        # self.assertTrue(funcList[1].start == 23)
        # self.assertTrue(funcList[1].end == 29)

        # funcList = self.chunk20.functions
        # #self.debugFunctions(funcList)
        # #print("FUNCTIONS")
        # #print(funcList)
        # self.assertTrue(len(funcList) == 4)
        # self.assertTrue(funcList[0].method ==  "has_pending_exclusive_lock")
        # self.assertTrue(funcList[1].method ==  "~MDL_lock")
        # self.assertTrue(funcList[2].method ==  "MDL_global_lock")
        # self.assertTrue(funcList[3].method ==  "is_empty")

        # funcList = self.chunk26.functions
        # #self.debugFunctions(funcList)
        # self.assertTrue(len(funcList) == 1)
        # self.assertTrue(funcList[0].method ==  "NO_FUNC_CONTEXT")
        # self.assertTrue(len(funcList[0].assertionList) == 8)

        #funcList = self.chunk28.functions
        #self.debugFunctions(funcList)

        #self.assertTrue(len(funcList) == 6)

        #funcList = self.chunk30.functions
        #self.debugFunctions(funcList)
        #self.assertTrue(len(funcList) == 2)

        #self.assertTrue(funcList[0].method ==  "_ccv_rgb_to_yuv")
        #testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 0, 'ut_a Dels': 0}
        #self.assertTrue(testDict,funcList[0].keywordDictionary)
        #self.assertTrue(len(funcList[0].assertionList) == 0)

        #self.assertTrue(funcList[1].method ==  "ccv_color_transform")
        #testDict = { 'ut_ad Adds': 0, 'assert Dels': 0, 'ut_ad Dels': 0, 'ut_a Adds': 0, 'assert Adds': 2, 'ut_a Dels': 0}
        #self.assertTrue(testDict,funcList[1].keywordDictionary)
        #self.assertTrue(len(funcList[1].assertionList) == 2)

        #This one was always alright, I just didn't read it correctly...
        #funcList = self.chunk34.functions
        #self.debugFunctions(funcList)
        #self.assertTrue(len(funcList) == 0)

if __name__=="__main__":
    unittest.main()