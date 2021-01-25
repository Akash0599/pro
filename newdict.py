import pandas as pd

"""class Tba:

    def __init__(self,headerId,detailId,msgType,msgId,targetMsgId,referenceId,TBAId,lotId,notifType,EffectiveDate,tradeDate,settlementDate,TBAsize,price,
                 TBAcusip,deliveryDate,origFace,currentFace,factor,poolNumber,netAmount,principal,accruedInterest,poolSecId,poolCusip,poolInterestStartDate,
                 poolMaturity,TBAlongDesc,coupon,externalId,name1,name2,address1,address2,address3,custContact,fax,email,address,terminator,contact,tradeStatus,
                 tradeStips,reasonCode,numGM,xref,subAccount,possibleDup,internalNumber):

        self.headerId = headerId
        self.detailId = detailId
        self.msgType = msgType
        self.msgId = msgId
        self.targetMsgId = targetMsgId
        self.referenceId = referenceId
        self.TBAId = TBAId
        self.lotId = lotId
        self.notifType = notifType
        self.EffectiveDate = EffectiveDate
        self.tradeDate = tradeDate
        self.settlementDate = settlementDate
        self.TBAsize = TBAsize
        self.price = price
        self.TBAcusip = TBAcusip
        self.deliveryDate = deliveryDate
        self.origFace = origFace
        self.currentFace = currentFace
        self.factor = factor
        self.poolNumber = poolNumber
        self.netAmount = netAmount
        self.principal = principal
        self.accruedInterest = accruedInterest
        self.poolSecId = poolSecId
        self.poolCusip = poolCusip
        self.poolInterestStartDate = poolInterestStartDate
        self.poolMaturity = poolMaturity
        self.TBAlongDesc = TBAlongDesc
        self.coupon = coupon
        self.externalId = externalId
        self.name1 = name1
        self.name2 = name2
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.custContact = custContact
        self.fax = fax
        self.email = email
        self.address = address
        self.terminator = terminator
        self.contact = contact
        self.tradeStatus = tradeStatus
        self.tradeStips = tradeStips
        self.reasonCode = reasonCode
        self.numGM = numGM
        self.xref = xref
        self.subAccount = subAccount
        self.possibleDup = possibleDup
        self.internalNumber = internalNumber


s1 = Tba(62031, 201850, "ON", "NULL", "NULL", "NULL", 7782799, 1.1, "EML", "00:00.0",  "00:00.0", "00:00.0", 46000000, 108.15625, "01F042665", "00:00.0", 19141382, 10000000.04, 0.52242832, "CA2206", 10828125.04, 10815625.04, 12500, 1104031, "3140Q9NY5", "00:00.0", "00:00.0", "FNMA TBA 30 Yr  4.50% Jun Single Family", 4.5, 5529990, "Northwestern Mutual Life Insur", "NULL", "720 East Wisconsin Avenue", "NULL", "Milwaukee, WI 53202", "Brian Yeazel", "NULL", "Lindacorrell@northwesternmutual.com", "Lindacorrell@northwesternmutual.com", 10, "NULL", "CXL", "MAX Pieces(1); MAX Pools(1)", "NULL", 10, "NULL", "NULL", "NULL", "G22703")
s2 = Tba(62032, 201851, "ON", "NULL", "NULL", "NULL", 7782800, 1.1,"EML", "00:00.0", "00:00.0", "00:00.0", 46000000, 108.15625, "01F042665", "00:00.0",19141382,10000000.04,0.52242832,"CA2206",10828125.04,10815625.04,12500, 1104031,"3140Q9NY5","00:00.0","00:00.0","FNMA TBA 30 Yr  4.50% Jun Single Family",4.5,5529990,"Northwestern Mutual Life Insur","NULL","720 East Wisconsin Avenue","NULL","Milwaukee,WI 53202","Brian Yeazel","NULL","Lindacorrell@northwesternmutual.com","Lindacorrell@northwesternmutual.com",10,"NULL","CXL","MAX Pieces(1); MAX Pools(1)","NULL",10,"NULL","NULL","NULL","G22703")
s3 = Tba(62033,201852,"ON","NULL","NULL","NULL",7782803,1.1,"EML","00:00.0","00:00.0","00:00.0",46000000,108.15625, "01F042665", "00:00.0",19141382,10000000.04,0.52242832,"CA2206",10828125.04,10815625.04,12500,1104031,"3140Q9NY5","00:00.0","00:00.0","FNMA TBA 30 Yr  4.50% Jun Single Family",4.5,5529990,"Northwestern Mutual Life Insur","NULL","720 East Wisconsin Avenue","NULL","Milwaukee, WI 53202","Brian Yeazel","NULL","Lindacorrell@northwesternmutual.com","Lindacorrell@northwesternmutual.com",10,"NULL","CXL","MAX Pieces(1); MAX Pools(1)","NULL",10,"NULL","NULL","NULL","G22703")
s4 = Tba(62035,201854,"ON","NULL","NULL","NULL",7761000,1.1,"EML","00:00.0","00:00.0","00:00.0",46000000,108.15625, "01F042665", "00:00.0",10238226,5999999.93,0.58603902,"CA3225",6496874.93,6489374.93,7500,1184594,"3140QASP6","00:00.0","00:00.0","FNMA TBA 30 Yr  4.50% Jun Single Family",4.5,5529990,"Northwestern Mutual Life Insur","NULL","720 East Wisconsin Avenue","NULL","Milwaukee, WI 53202","Brian Yeazel","NULLL","indacorrell@northwesternmutual.com","Lindacorrell@northwesternmutual.com",6,"NULL","CXL","MAX Pieces(1); MAX Pools(1)","NULL",6,"NULL","NULL","NULL","G22703")
s5 = Tba(62523,204270,"ON","NULL","NULL","NULL",7810034,1.1,"EML","00:00.0","00:00.0","00:00.0",6019756,105.8046875, "01F022675", "00:00.0",6019756,6019756,1,"QB1496",6374618.52,6369184.02,5434.5,1192183,"3133A7UV9","00:00.0","00:00.0","FNMA TBA 30 Yr  2.50% Jul Single Family",2.5,5404680,"Cherry Hill Mortgage Management","NULL","623 5th Ave","24th Floor","New York,NY 10020", "NULL", "NULL","Jerry.DuPont@avmltd.com","Jerry.DuPont@avmltd.com",9999,"NULL","CXL","MAX Pools(1)","NULL",6,"NULL","NULL","NULL","NULL")
s6 = Tba(62780,205884,"ON","NULL","NULL","NULL",7761922,1.1,"EML","00:00.0","00:00.0","00:00.0",5000000,102.90625, "01F020471", "00:00.0",5000000,5000000,1,"SB8057",5149479.17,5145312.5,4166.67,1188165,"3132D55S7","00:00.0","00:00.0","FNMA TBA 15 Yr  2.00% Jul Single Family",2,"3010350CU ","Investment Solutions","NULL","9701 Renner Boulevard","Suite 350","Lenexa, KS 66219-9739","Ilya Katsman","NULL","Jbecker@cu-isi.org","Jbecker@cu-isi.org",5,"NULL","CXL","MAX Pools(1)","NULL",5,"NULL","NULL","NULL","NULL")
s7 = Tba(63344,208928,"ON","NULL","NULL","NULL",7797525,1.1,"EML","00:00.0","00:00.0","00:00.0",5000000,102.9375, "01F020489", "00:00.0",5000000,5000000,1,"MA4123",5151319.44,5146875,4444.44,1195749,"31418DSM5","00:00.0","00:00.0","FNMA TBA 15 Yr  2.00% Aug Single Family",2,3010350,"CU Investment Solutions","NULL","9701 Renner Boulevard","Suite 350","Lenexa, KS 66219-9739","Ilya Katsman","NULL","Jbecker@cu-isi.org","Jbecker@cu-isi.org",5,"NULL","CXL","MAX Pools(1)","NULL",5,"NULL","NULL","NULL","NULL")
s8 = Tba(64627,215739,"ON","NULL","NULL","NULL",7844153,1.1,"EML","00:00.0","00:00.0","00:00.0",5000000,103.46875, "01F0204A4", "00:00.0",5181426,5000000.29,0.96498537,"MA4074",5178437.8,5173437.8,5000,1187056,"31418DQ47","00:00.0","00:00.0","FNMA TBA 15 Yr  2.00% Oct Single Family",2,3010350,"CU Investment Solutions","NULL","9701 Renner Boulevard","Suite 350","Lenexa, KS 66219-9739","Ilya Katsman","NULL","Jbecker@cu-isi.org","Jbecker@cu-isi.org",5,"NULL","CXL","MAX Pools(1)","NULL",5,"NULL","NULL","NULL","NULL")
s9 = Tba(64627,215739,"ON","NULL","NULL","NULL",7844153,1.1,"EML","00:00.0","00:00.0","00:00.0",5000000,103.46875, "01F0204A4", "00:00.0",5181426,5000000.29,0.96498537,"MA4074",5178437.8,5173437.8,5000,1187056,"31418DQ47","00:00.0","00:00.0","FNMA TBA 15 Yr  2.00% Oct Single Family",2,3010350,"CU Investment Solutions","NULL","9701 Renner Boulevard","Suite 350","Lenexa, KS 66219-9739","Ilya Katsman","NULL","Jbecker@cu-isi.org","Jbecker@cu-isi.org",5,"NULL","CXL","MAX Pools(1)","NULL",5,"NULL","NULL","NULL","NULL")

print(s2.headerId)"""


s1 = pd.read_excel("tba.xlsx")
print(s1["headerId"])





