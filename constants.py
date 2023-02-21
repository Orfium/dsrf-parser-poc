SOUND_RECORDING_HEADERS = [
    "AssetID",
    "Title",
    "Artist",
    "Writers",
    "ISRC",
    "Views",
    "Tag"
]

COMPOSITION_HEADERS = [
    "AssetID",
    "Title",
    "Artist",
    "Writers",
    "ISWC",
    "Views",
    "Tag"
]

RECORDS = {
    "HEAD": ["MessageVersion", "Profile", "ProfileVersion", "MessageId", "MessageCreatedDateTime", "FileNumber", "NumberOfFiles", "UsageStartDate", "UsageEndDate", "SenderPartyId", "SenderName", "ServiceDescription", "RecipientPartyId", "RecipientName", "RepresentedRepertoire"],
    "SY01.02": ["SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel", "UseType", "Territory", "ServiceDescription", "TotalUsages", "Subscribers", "CurrencyOfReporting", "NetRevenue", "IndirectValue", "CurrencyOfTransaction", "ExchangeRate"],
    "SY02.03": ["SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel", "UseType", "Territory", "ServiceDescription", "Usages", "Users", "Currency", "NetRevenue", "RightsController", "RightsControllerPartyId", "AllocatedUsages", "AllocatedRevenue", "AllocatedNetRevenue", "RightsType", "ContentCategory", "ExchangeRateBaseCurrency", "ExchangeRate", "RightsTypePercentage"],
    "SY04.02": ["SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel", "UseType", "Territory", "ServiceDescription", "SubscriberType", "Subscribers", "SubPeriodStartDate", "SubPeriodEndDate", "TotalUsagesInSubPeriod", "TotalUsagesInReportingPeriod", "CurrencyOfReporting", "CurrencyOfTransaction", "ExchangeRate", "ConsumerPaidUnitPrice", "NetRevenue", "MusicUsagePercentage"],
    "SY05.03": ["SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel", "UseType", "Territory", "ServiceDescription", "RightsController", "RightsControllerPartyId", "RightsType", "TotalUsages", "AllocatedUsages", "MusicUsageRatio", "AllocatedNetRevenue", "AllocatedRevenue", "RightsControllerMarketShare", "CurrencyOfReporting", "CurrencyOfTransaction", "ExchangeRate", "SubPeriodStartDate", "SubPeriodEndDate", "ContentCategory", "RightsTypePercentage"],

    "RE02": ["BlockId", "ReleaseReference", "DspSubReleaseId", "ProprietarySubReleaseId", "UsedResources"],
    "RE01.02": ["BlockId", "ReleaseReference", "DspReleaseId", "ProprietaryReleaseId", "CatalogNumber", "ICPN", "DisplayArtistName", "DisplayArtistPartyId", "Title", "SubTitle", "ReleaseType", "LabelName", "PLine", "DataProviderName", "ReleaseDate"],
    "AS01.02": ["BlockId", "ResourceReference", "DspResourceId", "ISRC", "Title", "SubTitle", "DisplayArtistName", "DisplayArtistPartyId", "Duration", "ResourceType", "IsMasterRecording", "IsSubjectToOwnershipConflict", "LastConflictCheck"],
    "AS02.03": ["BlockId", "ResourceReference", "DspResourceId", "ISRC", "Title", "SubTitle", "DisplayArtistName", "DisplayArtistPartyID", "Duration", "ResourceType", "ISWC", "ComposerAuthorName", "ComposerAuthorPartyId", "ArrangerName", "ArrangePartyID", "MusicPublisherName", "MusicPublisherPartyId", "WorkContributorName", "WorkContributorPartyId", "ProprietaryWorkId", "IsMasterRecording"],
    "SU02.02": ["BlockId", "SummaryRecordId", "SalesTransactionId", "TransactedRelease", "TransactedResource", "IsRoyaltyBearing", "NumberOfStreams", "PriceConsumerPaidExcSalesTax", "PromotionalActivity", "UseType"],
    "SU01.02": ["BlockId", "SummaryRecordId", "SalesTransactionId", "TransactedRelease", "TransactedResource", "IsRoyaltyBearing", "SalesUpgrade", "Usages", "Returns", "PriceConsumerPaidExcSalesTax", "PromotionalActivity", "UseType"],
    "FOOT": ["NumberOfLinesInFile", "NumberOfLinesInReport", "NumberOfSummaryRecords", "NumberOfBlocksInFile", "NumberOfBlocksInReport"],
    "SR01.01": ["SummaryRecordId", "DspResourceId", "ISRC", "Title", "SubTitle", "DisplayArtistName", "DisplayArtistPartyId", "Duration", "ResourceType", "ProperaryWorkId", "ISWC", "ComposerAuthor", "ComposerAuthorPartyId", "Arranger", "ArrangerPartyId", "MusicPublisher", "MusicPublisherPartyId", "WorkContributor", "WorkContributorPartyId", "DspReleaseId", "ProprietaryReleaseId", "CatalogNumber", "ICPN", "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId", "ReleaseTitle", "ReleaseSubTitle", "ReleaseType", "ReleaseLabel", "PLine", "ReleaseDataProvider", "NumberOfTransactedResources", "SalesTransactionId", "IsRoyaltyBearing", "SalesUpgrade", "Dowloads", "Returns", "PriceConsumerPaidExcSalesTax", "CalculatedPriceConsumer", "PaidForResourceExcSalesTax", "PromotionalActivity", "ReleaseDate", "UseType", "PriceConsumerPaidExcSalesTax"],
    "MW01.02": ["BlockId", "DspWorkId", "ISWC", "Title", "SubTitle", "ComposerAuthorName", "ComposerAuthorPartyId", "ArrangerName", "ArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId", "WorkContributorName", "WorkContributorPartyId", "DataProviderName", "ProprietaryWorkId", "ResourceReference", "ParentLicensorDataRecordId", "ParentMasterlistId"],
    "SRFO": ["NumberOfLinesInReport", "NumberOfSummaryRecords"],
}

HEAD_RELEASES = ["RE01.02"]
RESOURCES = ["AS01.02", "AS02.03"]
SALES_USAGES = ["SU02.02", "SU01.02"]