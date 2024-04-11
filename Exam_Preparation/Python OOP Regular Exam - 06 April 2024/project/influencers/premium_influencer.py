from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT = 0.85
    HIGH_BUDGET_MULTIPLIER = 1.5
    LOW_BUDGET_MULTIPLIER = 0.8

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        return float(campaign.budget * self.INITIAL_PAYMENT)

    def reached_followers(self, campaign_type: str):
        reached_followers = None
        if campaign_type == "HighBudgetCampaign":
            reached_followers = (self.followers * self.engagement_rate) * self.HIGH_BUDGET_MULTIPLIER
        elif campaign_type == "LowBudgetCampaign":
            reached_followers = (self.followers * self.engagement_rate) * self.LOW_BUDGET_MULTIPLIER

        if reached_followers:
            return int(reached_followers)


