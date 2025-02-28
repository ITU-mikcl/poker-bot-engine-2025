public class bot  {
    public static final String BOT_NAME = "Mus";

    public static int act(Observable obs) throws Exception {
        if (isLogicalToRaise(obs)) {
            if (obs.getMyHandType().getValue() > 3) {
                return obs.getMaxRaise();
            } else {
                return obs.getMinRaise();
            }
        } else {
            return checkFold(obs);
        }
    }

    private static boolean isLogicalToRaise(Observable obs) {
        return obs.getMyHandType().getValue() > obs.getBoardHandType().getValue();
    }

    private static boolean hasAnyoneRaised(Observable obs) {
        return obs.getCallSize() > obs.getMinRaise();
    }

    private static int checkFold(Observable obs) {
        return hasAnyoneRaised(obs) ? 0 : 1;
    }
 }