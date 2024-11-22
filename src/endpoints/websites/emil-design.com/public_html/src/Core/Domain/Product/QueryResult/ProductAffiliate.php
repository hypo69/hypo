<?php
/**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Open Software License (OSL 3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/OSL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)
 */

declare(strict_types=1);

namespace PrestaShop\PrestaShop\Core\Domain\Product\QueryResult;

/**
 * Holds product details
 */
class ProductAffiliate
{
    /**
     * @var string
     */
    private $affiliate_text;

    /**
     * @var string
     */
    private $affiliate_short_link;

    /**
     * @var string
     */
    private $affiliate_summary;

    /**
     * @var string
     */
    private $affiliate_summary_2;

    /**
     * @var string
     */
    private $affiliate_image_small;

    /**
     * @var string
     */
    private $affiliate_image_medium;

    /**
     * @var string
     */
    private $affiliate_image_large;
    
    
    /**
     * @param string $affiliate_text
     * @param string $affiliate_short_link
     * @param string $affiliate_summary
     * @param string $affiliate_summary_2
     * @param string $affiliate_image_small
     * @param string $affiliate_image_medium
     * @param string $affiliate_image_large
     */
    public function __construct(
        string $affiliate_text,
        string $affiliate_short_link,
        string $affiliate_summary,
        string $affiliate_summary_2,
        string $affiliate_image_small,
        string $affiliate_image_medium,
        string $affiliate_image_large
    ) {
        $this->affiliate_text = $affiliate_text;
        $this->affiliate_short_link = $affiliate_short_link;
        $this->affiliate_summary = $affiliate_summary;
        $this->affiliate_summary_2 = $affiliate_summary_2;
        $this->affiliate_image_small = $affiliate_image_small;
        $this->affiliate_image_medium = $affiliate_image_medium;
        $this->affiliate_image_large = $affiliate_image_large;
    }

    /**
     * @return string
     */
    public function getAffiliate_text(): string
    {
        return $this->affiliate_text;
    }

    /**
     * @return string
     */
    public function getAffiliateShortLink(): string
    {
        return $this->affiliate_short_link;
    }

    /**
     * @return string
     */
    public function getAffiliateSummary(): string
    {
        return $this->affiliate_summary;
    }

    /**
     * @return string
     */
    public function getAffiliateSummary2(): string
    {
        return $this->affiliate_summary_2;
    }

    /**
     * @return string
     */
    public function getAffiliateImageSmall(): string
    {
        return $this->affiliate_image_small;
    }

        /**
     * @return string
     */
    public function getAffiliateImageMedium(): string
    {
        return $this->affiliate_image_medium;
    }

            /**
     * @return string
     */
    public function getAffiliateImageLarge(): string
    {
        return $this->affiliate_image_large;
    }
}
