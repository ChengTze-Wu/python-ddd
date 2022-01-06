from decimal import Decimal
from seedwork.application.command_handlers import CommandResult
from seedwork.application.decorators import command_handler
from src.modules.bidding.domain.entities import Bidding
from src.modules.bidding.domain.repositories import ListingRepository


class RetractBidCommand:
    buyer_id: str
    amount: Decimal
    currency: str = "USD"


@command_handler
def retract_bid(
    command: PlaceBidCommand, repository: ListingRepository
) -> CommandResult:
    listing = repository.get_by_id(listing_id=command.listing_id)
    if listing is None:
        return CommandResult.failed("Listing does not exist")

    buyer = Buyer(id=command.buyer_id)
    money = Money(amount=command.amount)
    bid = Bid(buyer=buyer, money=money)
    listing.place_bid(bid)
    repository.update(listing)

    return CommandResult.ok()