// src/data/bankData.js
import KB from "@/assets/BankLogo/bankName=KB국민.svg";
import IBK from "@/assets/BankLogo/bankName=IBK기업.svg";
import KBA from "@/assets/BankLogo/bankName=KB증권.svg";
import KDB from "@/assets/BankLogo/bankName=KDB산업.svg";
import KEB from "@/assets/BankLogo/bankName=KEB외환.svg";
import NH from "@/assets/BankLogo/bankName=NH농협.svg";
import NHI from "@/assets/BankLogo/bankName=NH투자증권.svg";
import SBI from "@/assets/BankLogo/bankName=SBI저축.svg";
import SC from "@/assets/BankLogo/bankName=SC제일.svg";
import KN from "@/assets/BankLogo/bankName=경남.svg";
import GJ from "@/assets/BankLogo/bankName=광주.svg";
import DG from "@/assets/BankLogo/bankName=대구.svg";
import BS from "@/assets/BankLogo/bankName=부산.svg";
import FOREST from "@/assets/BankLogo/bankName=산림조합.svg";
import NEW from "@/assets/BankLogo/bankName=새마을.svg";
import SH from "@/assets/BankLogo/bankName=수협.svg";
import SINHAN from "@/assets/BankLogo/bankName=신한.svg";
import SINHY from "@/assets/BankLogo/bankName=신협.svg";
import CITY from "@/assets/BankLogo/bankName=씨티.svg";
import URI from "@/assets/BankLogo/bankName=우리.svg";
import POST from "@/assets/BankLogo/bankName=우정사업본부.svg";
import SB from "@/assets/BankLogo/bankName=저축은행.svg";
import JB from "@/assets/BankLogo/bankName=전북.svg";
import JJ from "@/assets/BankLogo/bankName=제주.svg";
import K from "@/assets/BankLogo/bankName=케이뱅크.svg";
import TOSS from "@/assets/BankLogo/bankName=토스뱅크.svg";
import KAKAO from "@/assets/BankLogo/bankName=카카오뱅크.svg";
import HANA from "@/assets/BankLogo/bankName=하나.svg";
import HANTU from "@/assets/BankLogo/bankName=한국투자증권.svg";



// 은행 데이터
export const banks = [
    { id: "BK_KB_Symbol", name: "KB국민", logo: KB},
    { id: "BK_SHINHAN_Symbol", name: "신한", logo: SINHAN },
    { id: "BK_HANA_Symbol", name: "하나", logo: HANA },
    { id: "BK_WOORI_Symbol", name: "우리", logo: URI },
    { id: "BK_NH_Symbol", name: "NH농협", logo: NH },
    { id: "BK_IBK_Symbol", name: "IBK기업", logo: IBK },
    { id: "BK_KDB_Symbol", name: "KDB산업", logo: KDB },
    { id: "BK_CU_Symbol", name: "신협", logo: SINHY },
    { id: "BK_SC_Symbol", name: "SC제일", logo: SC },
    { id: "BK_EPOST_Symbol", name: "우정사업본부", logo: POST },
    { id: "BK_BUSAN_Symbol", name: "부산", logo: BS },
    { id: "BK_DAEGU_Symbol", name: "iM뱅크", logo: null },
    { id: "BK_SH_Symbol", name: "SH수협", logo: SH },
    { id: "BK_KYOUNGNAM_Symbol", name: "경남", logo: KN },
    { id: "BK_KAKAO_Symbol", name: "카카오뱅크", logo: KAKAO },
    { id: "BK_KWANGJU_Symbol", name: "광주", logo: GJ },
    { id: "BK_TOSS_Symbol", name: "토스뱅크", logo: TOSS },
    { id: "BK_JEONBUK_Symbol", name: "전북", logo: JB },
    { id: "BK_K_Symbol", name: "케이뱅크", logo: K },
    { id: "BK_JEJU_Symbol", name: "제주", logo: JJ },
  ];
  
  // 저축은행 데이터
  export const savingsBanks = [
    { id: "SB_BNK_Symbol", name: "BNK저축", logo: null },
    { id: "SB_CK_Symbol", name: "CK저축", logo: null },
    { id: "SB_DB_Symbol", name: "DB저축", logo: null },
    { id: "SB_DH_Symbol", name: "DH저축", logo: null },
    { id: "SB_HB_Symbol", name: "HB저축", logo: null },
    { id: "SB_IBK_Symbol", name: "IBK저축", logo: null },
    { id: "SB_JT_Symbol", name: "JT저축", logo: null },
    { id: "SB_JTCHINAE_Symbol", name: "JT친애저축", logo: null },
    { id: "SB_KB_Symbol", name: "KB저축", logo: KB },
    { id: "SB_NH_Symbol", name: "NH저축", logo: NH },
    { id: "SB_OK_Symbol", name: "OK저축", logo: null },
    { id: "SB_OSB_Symbol", name: "OSB저축", logo: null },
    { id: "SB_SBI_Symbol", name: "SBI저축", logo: null },
    { id: "SB_SNT_Symbol", name: "SNT저축", logo: null },
    { id: "SB_COREA_Symbol", name: "고려저축", logo: null },
    { id: "SB_KOOKJE_Symbol", name: "국제저축", logo: null },
    { id: "SB_KUMHWA_Symbol", name: "금화저축", logo: null },
    { id: "SB_NAMYANG_Symbol", name: "남양저축", logo: null },
    { id: "SB_DAOL_Symbol", name: "다올저축", logo: null },
    { id: "SB_DAEMYUNG_Symbol", name: "대명저축", logo: null },
    { id: "SB_DAEBAEK_Symbol", name: "대백저축", logo: null },
    { id: "SB_DAISHIN_Symbol", name: "대신저축", logo: null },
    { id: "SB_DAEAH_Symbol", name: "대아저축", logo: null },
    { id: "SB_DAEWON_Symbol", name: "대원저축", logo: null },
    { id: "SB_DAEHAN_Symbol", name: "대한저축", logo: null },
    { id: "SB_DOUBLE_Symbol", name: "더블저축", logo: null },
    { id: "SB_THEK_Symbol", name: "더케이저축", logo: null },
    { id: "SB_DONGYANG_Symbol", name: "동양저축", logo: null },
    { id: "SB_DONGWONJEIL_Symbol", name: "동원제일저축", logo: null },
    { id: "SB_DREAM_Symbol", name: "드림저축", logo: null },
    { id: "SB_RAON_Symbol", name: "라온저축", logo: null },
    { id: "SB_MUSTSAMIL_Symbol", name: "머스트삼일", logo: null },
    { id: "SB_MOA_Symbol", name: "모아저축", logo: null },
    { id: "SB_MK_Symbol", name: "민국저축", logo: null },
    { id: "SB_BARO_Symbol", name: "바로저축", logo: null },
    { id: "SB_BOORIM_Symbol", name: "부림저축", logo: null },
    { id: "SB_SAMJUNG_Symbol", name: "삼정저축", logo: null },
    { id: "SB_SAMHO_Symbol", name: "삼호저축", logo: null },
    { id: "SB_SANGSANGIN_Symbol", name: "상상인저축", logo: null },
    { id: "SB_SANGSANGINPLUS_Symbol", name: "상상인플러스", logo: null },
    { id: "SB_SERAM_Symbol", name: "세람저축", logo: null },
    { id: "SB_CENTRAL_Symbol", name: "센트럴저축", logo: null },
    { id: "SB_SOLBRAIN_Symbol", name: "솔브레인저축", logo: null },
    { id: "SB_SMART_Symbol", name: "스마트저축", logo: null },
    { id: "SB_SKY_Symbol", name: "스카이저축", logo: null },
    { id: "SB_STAR_Symbol", name: "스타저축", logo: null },
    { id: "SB_SHINHAN_Symbol", name: "신한저축", logo: null },
    { id: "SB_ASAN_Symbol", name: "아산저축", logo: null },
    { id: "SB_ANGUK_Symbol", name: "안국저축", logo: null },
    { id: "SB_ANYANG_Symbol", name: "안양저축", logo: null },
    { id: "SB_ACUON_Symbol", name: "애큐온저축", logo: null },
    { id: "SB_MS_Symbol", name: "엠에스저축", logo: null },
    { id: "SB_YOUNGJIN_Symbol", name: "영진저축", logo: null },
    { id: "SB_YEKARAM_Symbol", name: "예가람저축", logo: null },
    { id: "SB_OHSUNG_Symbol", name: "오성저축", logo: null },
    { id: "SB_OHTWO_Symbol", name: "오투저축", logo: null },
    { id: "SB_WOORIFIN_Symbol", name: "우리금융저축", logo: null },
    { id: "SB_WOORITOUJA_Symbol", name: "우리투자", logo: null }, // ID 수정
    { id: "SB_WOORI_Symbol", name: "우리저축", logo: null },
    { id: "SB_WELCOME_Symbol", name: "웰컴저축", logo: null },
    { id: "SB_UNION_Symbol", name: "유니온저축", logo: null },
    { id: "SB_YUANTA_Symbol", name: "유안타저축", logo: null },
    { id: "SB_YOONGCHANG_Symbol", name: "융창저축", logo: null },
    { id: "SB_INSUNG_Symbol", name: "인성저축", logo: null },
    { id: "SB_INCHEON_Symbol", name: "인천저축", logo: null },
    { id: "SB_CHOEUN_Symbol", name: "조은저축", logo: null },
    { id: "SB_CHOHEUNG_Symbol", name: "조흥저축", logo: null },
    { id: "SB_JINJU_Symbol", name: "진주저축", logo: null },
    { id: "SB_TRUE_Symbol", name: "참저축", logo: null },
    { id: "SB_CHUNGJU_Symbol", name: "청주저축", logo: null },
    { id: "SB_KIWOOMYES_Symbol", name: "키움예스저축", logo: null },
    { id: "SB_KIWOOM_Symbol", name: "키움저축", logo: null },
    { id: "SB_PEPPER_Symbol", name: "페퍼저축", logo: null },
    { id: "SB_PYUNGTAEK_Symbol", name: "평택저축", logo: null },
    { id: "SB_PURUN_Symbol", name: "푸른저축", logo: null },
    { id: "SB_HANA_Symbol", name: "하나저축", logo: null },
    { id: "SB_KOREAINVEST_Symbol", name: "한국투자저축", logo: null },
    { id: "SB_HANSUNG_Symbol", name: "한성저축", logo: null },
    { id: "SB_HANWHA_Symbol", name: "한화저축", logo: null },
    { id: "SB_HEUNGKUK_Symbol", name: "흥국저축", logo: null },
  ];
  