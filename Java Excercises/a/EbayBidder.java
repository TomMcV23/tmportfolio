public class EbayBidder {

  private EbayStrategy myStrategy;

  public void doSomeBidding() {
    myStrategy.doTheBiddingStrategy();
  }

  public EbayBidder() {
// Default strategy: non-sniping
    this.setNonSnipingStrategy();
  }

  public void setNonSnipingStrategy() {
    myStrategy = new NonSnipingStrategy();
  }

  public void setSnipingStrategy() {
    myStrategy = new SnipingStrategy();
  }

  public void setLateButNotOnASundayStrategy() {
    myStrategy = new LateButNotOnASundayStrategy();
  }

  public static void main(String[] args) {
    EbayBidder b = new EbayBidder();
    System.out.println("At the moment our bidder is using the default non-sniping strategy ...");
    b.doSomeBidding();
    System.out.println("Now our bidder is more aggressive, using the sniping strategy ...");
    b.setSnipingStrategy();
    b.doSomeBidding();
  }
}
