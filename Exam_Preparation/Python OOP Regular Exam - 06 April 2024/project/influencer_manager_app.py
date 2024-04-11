from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer,
                              "StandardInfluencer": StandardInfluencer}

    VALID_CAMPAIGN_TYPES = {"HighBudgetCampaign": HighBudgetCampaign,
                            "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES.keys():
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            self.influencers.append(self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate))
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        try:
            next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:
            self.campaigns.append(self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement))
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' "
                    f"does not meet the eligibility criteria for the campaign with ID {campaign_id}.")

        if influencer.calculate_payment(campaign) > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' "
                    f"has successfully participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        total_reached_followers = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                if campaign not in total_reached_followers.keys():
                    total_reached_followers[campaign] = 0

                total_reached_followers[campaign] += influencer.reached_followers(campaign.__class__.__name__)

        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers))
        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))

        available_campaigns = self.calculate_total_reached_followers()

        budget = f"$$ Campaign Statistics $$"
        for campaigns in sorted_campaigns:
            budget += (f"\n  * Brand: {campaigns.brand}, "
                       f"Total influencers: {len(campaigns.approved_influencers)}, "
                       f"Total budget: ${campaigns.budget:.2f}, "
                       f"Total reached followers: "
                       f"{available_campaigns[campaigns] if campaigns in available_campaigns else 0}")

        return budget
